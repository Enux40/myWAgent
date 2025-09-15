#!/usr/bin/env python3
"""
GitHub Repository Management Script

This script demonstrates how to create repositories using the GitHub API integration.
"""

import os
import sys
from datetime import datetime
from src.github_api import GitHubAPI
from src.logger import logger


def create_test_repository():
    """Create a test repository with current timestamp."""
    github_api = GitHubAPI()
    
    # Get user info first to verify API connection
    user_info = github_api.get_user_info()
    if not user_info:
        logger.error("Failed to connect to GitHub API. Please check your GITHUB_API_TOKEN.")
        return False
    
    logger.info(f"Connected to GitHub as: {user_info.get('login', 'Unknown')}")
    
    # Create a test repository
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    repo_name = f"test-repo-{timestamp}"
    description = f"Test repository created by myWAgent on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    logger.info(f"Creating repository: {repo_name}")
    repo_data = github_api.create_repository(
        name=repo_name,
        description=description,
        private=False,  # Make it public for testing
        auto_init=True
    )
    
    if repo_data:
        logger.info(f"✅ Repository created successfully!")
        logger.info(f"📁 Repository name: {repo_data['name']}")
        logger.info(f"🔗 Repository URL: {repo_data['html_url']}")
        logger.info(f"📝 Description: {repo_data['description']}")
        return True
    else:
        logger.error("❌ Failed to create repository")
        return False


def list_user_repositories():
    """List the user's repositories."""
    github_api = GitHubAPI()
    
    logger.info("Fetching user repositories...")
    repos = github_api.list_repositories(per_page=10, page=1)
    
    if repos:
        logger.info(f"📚 Found {len(repos)} repositories:")
        for i, repo in enumerate(repos, 1):
            logger.info(f"  {i}. {repo['name']} - {repo['html_url']}")
            if repo['description']:
                logger.info(f"     Description: {repo['description']}")
        return True
    else:
        logger.error("❌ Failed to fetch repositories")
        return False


def main():
    """Main function to demonstrate GitHub repository management."""
    logger.info("🚀 Starting GitHub Repository Management Demo")
    
    # Check if GitHub API token is configured
    if not os.getenv("GITHUB_API_TOKEN"):
        logger.error("❌ GITHUB_API_TOKEN environment variable is not set.")
        logger.error("Please set your GitHub Personal Access Token in the .env file:")
        logger.error("GITHUB_API_TOKEN=your_token_here")
        return sys.exit(1)
    
    try:
        # List existing repositories
        logger.info("\n📋 Step 1: Listing existing repositories")
        list_user_repositories()
        
        # Create a new test repository
        logger.info("\n🆕 Step 2: Creating a new test repository")
        create_test_repository()
        
        logger.info("\n✅ Demo completed successfully!")
        
    except Exception as e:
        logger.error(f"❌ Demo failed with error: {e}")
        return sys.exit(1)


if __name__ == "__main__":
    main()