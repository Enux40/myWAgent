import logging
import os
from config import settings

# Ensure logs directory exists
os.makedirs(os.path.dirname(settings.LOG_FILE_PATH), exist_ok=True)

logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(settings.LOG_FILE_PATH), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)
