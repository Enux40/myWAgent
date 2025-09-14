#!/usr/bin/env python3
"""
Validation script for myWAgent project.
Run this to verify your installation is working correctly.
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is adequate."""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is adequate (3.8+)")
        return True
    else:
        print("❌ Python 3.8+ is required")
        return False

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("\nChecking dependencies...")
    
    required_packages = ['requests', 'python-dotenv', 'beautifulsoup4', 'apscheduler']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'python-dotenv':
                import dotenv
            elif package == 'beautifulsoup4':
                import bs4
            else:
                __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nTo install missing packages, run:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def check_project_structure():
    """Check if project structure is correct."""
    print("\nChecking project structure...")
    
    required_files = [
        'main.py',
        'requirements.txt',
        'README.md',
        'config/settings.py',
        'config/sources.py',
        'src/whatsapp_api.py',
        'src/content_scraper.py',
        'src/content_generator.py',
        'src/logger.py',
        'src/scheduler.py',
        'src/whatsapp_poster.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - missing")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def check_env_setup():
    """Check environment setup."""
    print("\nChecking environment setup...")
    
    if os.path.exists('.env'):
        print("✅ .env file exists")
        
        # Check if it's the example file (should be replaced)
        with open('.env', 'r') as f:
            content = f.read()
            if 'your_whatsapp_business_api_token_here' in content:
                print("⚠️  .env file contains example values - replace with real credentials")
                return False
            else:
                print("✅ .env file appears to have real credentials")
                return True
    elif os.path.exists('.env.example'):
        print("⚠️  .env.example exists but .env is missing")
        print("   Copy .env.example to .env and add your API credentials")
        return False
    else:
        print("❌ No environment file found")
        print("   Create a .env file with your API credentials")
        return False

def test_imports():
    """Test if modules can be imported."""
    print("\nTesting module imports...")
    
    try:
        from config import settings
        print("✅ config.settings")
        
        from src.whatsapp_api import WhatsAppAPI
        print("✅ src.whatsapp_api")
        
        from src.content_scraper import scrape_all_sources
        print("✅ src.content_scraper")
        
        from src.logger import logger
        print("✅ src.logger")
        
        print("✅ All core modules import successfully")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def main():
    """Run all validation checks."""
    print("=== myWAgent Project Validation ===\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Project Structure", check_project_structure),
        ("Environment Setup", check_env_setup),
        ("Module Imports", test_imports)
    ]
    
    passed = 0
    total = len(checks)
    
    for name, check_func in checks:
        print(f"\n--- {name} ---")
        if check_func():
            passed += 1
        else:
            print(f"❌ {name} check failed")
    
    print(f"\n=== Validation Results: {passed}/{total} checks passed ===")
    
    if passed == total:
        print("\n🎉 All validation checks passed!")
        print("Your myWAgent installation is ready to use.")
        print("\nNext steps:")
        print("1. Run 'python main.py' for a one-time test")
        print("2. Run 'python src/scheduler.py' for daily automation")
    else:
        print(f"\n❌ {total - passed} validation checks failed.")
        print("Please fix the issues above before using the project.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)