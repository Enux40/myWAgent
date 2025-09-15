#!/usr/bin/env python3
"""
GitHub Repository Creation Demo

This script demonstrates the GitHub API functionality without requiring actual API tokens.
It shows the structure and methods available for repository management.
"""

from src.logger import logger
import os


def demo_github_functionality():
    """Demonstrate GitHub API functionality structure."""
    logger.info("🎭 GitHub Repository Management Demo (Simulation Mode)")
    logger.info("=" * 60)
    
    # Check if GitHub token is available
    github_token = os.getenv("GITHUB_API_TOKEN")
    
    if github_token:
        logger.info("✅ GITHUB_API_TOKEN found - Testing real API functionality")
        try:
            from src.github_api import GitHubAPI
            
            github_api = GitHubAPI()
            
            # Get user info
            logger.info("📋 Getting user information...")
            user_info = github_api.get_user_info()
            if user_info:
                logger.info(f"✅ Connected as: {user_info.get('login', 'Unknown')}")
                logger.info(f"📊 Public repos: {user_info.get('public_repos', 0)}")
                logger.info(f"👥 Followers: {user_info.get('followers', 0)}")
            
            # List repositories
            logger.info("\n📚 Listing repositories...")
            repos = github_api.list_repositories(per_page=3)
            if repos:
                logger.info(f"Found {len(repos)} recent repositories:")
                for i, repo in enumerate(repos, 1):
                    logger.info(f"  {i}. {repo['name']}")
                    logger.info(f"     🔗 {repo['html_url']}")
                    if repo['description']:
                        logger.info(f"     📝 {repo['description']}")
            
            # Demonstrate repository creation (commented out to avoid creating test repos)
            logger.info("\n🆕 Repository creation capability available!")
            logger.info("To create a repository, use:")
            logger.info("  github_api.create_repository('my-repo', 'Description', private=False)")
            
        except Exception as e:
            logger.error(f"❌ Error testing GitHub API: {e}")
    
    else:
        logger.info("⚠️  No GITHUB_API_TOKEN found - Running in simulation mode")
        logger.info("")
        logger.info("🔧 Available GitHub API Methods:")
        logger.info("  📝 create_repository(name, description, private=False)")
        logger.info("  📋 list_repositories(per_page=30, page=1)")
        logger.info("  👤 get_user_info()")
        logger.info("")
        logger.info("📋 Example Usage:")
        logger.info("  # Create a new repository")
        logger.info("  github_api = GitHubAPI()")
        logger.info("  repo = github_api.create_repository(")
        logger.info("      name='my-awesome-project',")
        logger.info("      description='A cool project created via API',")
        logger.info("      private=False")
        logger.info("  )")
        logger.info("")
        logger.info("🔑 To use real GitHub API:")
        logger.info("  1. Get a GitHub Personal Access Token")
        logger.info("  2. Add GITHUB_API_TOKEN=your_token to .env file")
        logger.info("  3. Run this demo again")
    
    logger.info("\n" + "=" * 60)
    logger.info("✅ Demo completed successfully!")


if __name__ == "__main__":
    demo_github_functionality()