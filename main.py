from src.whatsapp_api import WhatsAppAPI
from src.github_api import GitHubAPI
from src.logger import logger
import sys


def test_whatsapp():
    """Test WhatsApp API functionality."""
    try:
        wa_api = WhatsAppAPI()
        test_message = "This is a test message from the WhatsApp AI Agent."
        logger.info("Sending test message...")
        result = wa_api.send_message(test_message)
        if result:
            logger.info(f"API Response: {result}")
        else:
            logger.error("Failed to send test message.")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")


def test_github():
    """Test GitHub API functionality."""
    try:
        github_api = GitHubAPI()
        
        # Get user info
        logger.info("Testing GitHub API connection...")
        user_info = github_api.get_user_info()
        if user_info:
            logger.info(f"Connected as: {user_info.get('login', 'Unknown')}")
            logger.info(f"Public repos: {user_info.get('public_repos', 0)}")
        else:
            logger.error("Failed to connect to GitHub API.")
            return
        
        # List repositories
        logger.info("Fetching user repositories...")
        repos = github_api.list_repositories(per_page=5)
        if repos:
            logger.info(f"Found {len(repos)} repositories (showing first 5):")
            for repo in repos:
                logger.info(f"  - {repo['name']}: {repo['html_url']}")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        logger.error("Please set GITHUB_API_TOKEN in your .env file")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "github":
            test_github()
        elif sys.argv[1] == "whatsapp":
            test_whatsapp()
        else:
            logger.info("Usage: python main.py [github|whatsapp]")
            logger.info("  github   - Test GitHub API functionality")
            logger.info("  whatsapp - Test WhatsApp API functionality")
    else:
        # Default behavior - test WhatsApp
        test_whatsapp()
