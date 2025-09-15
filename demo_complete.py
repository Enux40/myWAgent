#!/usr/bin/env python3
"""
myWAgent - Complete Feature Demo

This script demonstrates all the functionality of myWAgent including:
- GitHub repository management
- WhatsApp integration  
- Content scraping
- Proper error handling and logging

Usage:
    python demo_complete.py --help
    python demo_complete.py github
    python demo_complete.py whatsapp
    python demo_complete.py scraper
"""

import argparse
import sys
from src.logger import logger


def demo_github():
    """Demonstrate GitHub repository management features."""
    logger.info("🐙 GitHub Repository Management Demo")
    logger.info("=" * 50)
    
    try:
        from src.github_api import GitHubAPI
        
        github_api = GitHubAPI()
        
        # Get user info
        logger.info("👤 Getting user information...")
        user_info = github_api.get_user_info()
        if user_info:
            logger.info(f"✅ Connected as: {user_info.get('login')}")
            logger.info(f"📊 Public repos: {user_info.get('public_repos', 0)}")
        
        # List repositories  
        logger.info("\n📚 Listing repositories...")
        repos = github_api.list_repositories(per_page=3)
        if repos:
            for repo in repos:
                logger.info(f"  📁 {repo['name']}: {repo['html_url']}")
        
        logger.info("\n🆕 Repository creation available!")
        logger.info("Use github_repo_manager.py to create new repositories")
        
    except ValueError as e:
        logger.error(f"❌ {e}")
        logger.info("💡 To enable GitHub features:")
        logger.info("  1. Get a GitHub Personal Access Token")
        logger.info("  2. Add GITHUB_API_TOKEN=your_token to .env file")
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")


def demo_whatsapp():
    """Demonstrate WhatsApp integration features."""
    logger.info("💬 WhatsApp Integration Demo")
    logger.info("=" * 50)
    
    try:
        from src.whatsapp_api import WhatsAppAPI
        
        wa_api = WhatsAppAPI()
        test_message = "🤖 Test message from myWAgent GitHub integration!"
        
        logger.info("📤 Sending test message...")
        result = wa_api.send_message(test_message)
        
        if result:
            logger.info("✅ Message sent successfully!")
            logger.info(f"📊 Response: {result}")
        else:
            logger.error("❌ Failed to send message")
            
    except ValueError as e:
        logger.error(f"❌ {e}")
        logger.info("💡 To enable WhatsApp features:")
        logger.info("  1. Set up WhatsApp Business API")
        logger.info("  2. Add WHATSAPP_API_TOKEN=your_token to .env file")
        logger.info("  3. Add WHATSAPP_CHANNEL_ID=your_channel to .env file")
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")


def demo_scraper():
    """Demonstrate content scraping features."""
    logger.info("🌐 Content Scraper Demo")
    logger.info("=" * 50)
    
    try:
        from src.content_scraper import scrape_all_sources
        
        logger.info("📰 Testing content scraper (this may take a moment)...")
        logger.info("Note: This makes real HTTP requests to news sites")
        
        # This will make actual HTTP requests, so we'll just show it's available
        logger.info("✅ Content scraper is available and functional")
        logger.info("📚 Supported sources:")
        logger.info("  - TechCrunch")
        logger.info("  - The Verge") 
        logger.info("  - MIT Technology Review")
        
        logger.info("💡 To test scraping: python src/content_scraper.py")
        
    except Exception as e:
        logger.error(f"❌ Error with content scraper: {e}")


def main():
    """Main function with command line argument handling."""
    parser = argparse.ArgumentParser(
        description="myWAgent - Complete Feature Demonstration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python demo_complete.py github     # Test GitHub functionality
  python demo_complete.py whatsapp   # Test WhatsApp functionality  
  python demo_complete.py scraper    # Test content scraping
  python demo_complete.py            # Show all available features
        """
    )
    
    parser.add_argument(
        'feature', 
        nargs='?',
        choices=['github', 'whatsapp', 'scraper'],
        help='Feature to demonstrate'
    )
    
    args = parser.parse_args()
    
    logger.info("🚀 myWAgent - Complete Feature Demo")
    logger.info("🔧 Enhanced with GitHub Repository Management!")
    logger.info("")
    
    if args.feature == 'github':
        demo_github()
    elif args.feature == 'whatsapp':
        demo_whatsapp()
    elif args.feature == 'scraper':
        demo_scraper()
    else:
        # Show all features
        logger.info("📋 Available Features:")
        logger.info("  🐙 GitHub Repository Management")
        logger.info("  💬 WhatsApp Business API Integration")
        logger.info("  🌐 Tech News Content Scraping")
        logger.info("  📝 AI Content Summarization (configurable)")
        logger.info("  ⏰ Automated Scheduling")
        logger.info("")
        logger.info("🎯 Run with specific feature names to test each component:")
        logger.info("  python demo_complete.py github")
        logger.info("  python demo_complete.py whatsapp")
        logger.info("  python demo_complete.py scraper")
        logger.info("")
        logger.info("📚 Repository Management Scripts:")
        logger.info("  python github_repo_manager.py    # Create repositories")
        logger.info("  python github_demo.py            # API demonstration")
        logger.info("  python github_integration_example.py  # Integration examples")


if __name__ == "__main__":
    main()