import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Configurable parameters
API_URL = os.getenv("WHATSAPP_API_URL", "https://graph.facebook.com/v19.0")
API_TOKEN = os.getenv("WHATSAPP_API_TOKEN")
CHANNEL_ID = os.getenv("WHATSAPP_CHANNEL_ID", "YOUR_CHANNEL_ID")
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/app.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEFAULT_POST_TIME = os.getenv("DEFAULT_POST_TIME", "09:00")

if not API_TOKEN:
    raise ValueError("WHATSAPP_API_TOKEN environment variable is required.")
