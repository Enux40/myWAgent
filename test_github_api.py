#!/usr/bin/env python3
"""
Simple test for GitHub API functionality
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestGitHubAPI(unittest.TestCase):
    
    @patch('config.settings.GITHUB_API_TOKEN', 'test_token')
    @patch('src.github_api.requests.post')
    def test_create_repository_success(self, mock_post):
        """Test successful repository creation"""
        # Import after patching
        from src.github_api import GitHubAPI
        
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            'name': 'test-repo',
            'html_url': 'https://github.com/user/test-repo',
            'description': 'Test repository'
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # Test repository creation
        github_api = GitHubAPI()
        result = github_api.create_repository(
            name='test-repo',
            description='Test repository',
            private=False
        )
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'test-repo')
        self.assertEqual(result['html_url'], 'https://github.com/user/test-repo')
        
        # Verify API was called correctly
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        self.assertEqual(call_args[0][0], 'https://api.github.com/user/repos')
        self.assertIn('Authorization', call_args[1]['headers'])
        self.assertEqual(call_args[1]['json']['name'], 'test-repo')
    
    @patch('config.settings.GITHUB_API_TOKEN', 'test_token')
    @patch('src.github_api.requests.get')
    def test_get_user_info_success(self, mock_get):
        """Test successful user info retrieval"""
        # Import after patching
        from src.github_api import GitHubAPI
        
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'login': 'testuser',
            'public_repos': 5,
            'followers': 10
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Test user info retrieval
        github_api = GitHubAPI()
        result = github_api.get_user_info()
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['login'], 'testuser')
        self.assertEqual(result['public_repos'], 5)
    
    @patch('config.settings.GITHUB_API_TOKEN', 'test_token')
    @patch('src.github_api.requests.get')
    def test_list_repositories_success(self, mock_get):
        """Test successful repository listing"""
        # Import after patching
        from src.github_api import GitHubAPI
        
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'name': 'repo1', 'html_url': 'https://github.com/user/repo1'},
            {'name': 'repo2', 'html_url': 'https://github.com/user/repo2'}
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Test repository listing
        github_api = GitHubAPI()
        result = github_api.list_repositories(per_page=2)
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'repo1')
    
    @patch('config.settings.GITHUB_API_TOKEN', None)
    def test_missing_token_raises_error(self):
        """Test that missing token raises appropriate error"""
        from src.github_api import GitHubAPI
        
        with self.assertRaises(ValueError) as context:
            GitHubAPI()
        self.assertIn('GITHUB_API_TOKEN', str(context.exception))


if __name__ == '__main__':
    unittest.main()