import requests
from config import settings
from src.logger import logger


class WhatsAppAPI:
    def __init__(self):
        self.api_url = f"{settings.API_URL}/{settings.CHANNEL_ID}/messages"
        self.headers = {
            "Authorization": f"Bearer {settings.API_TOKEN}",
            "Content-Type": "application/json",
        }

    def send_message(self, message: str):
        payload = {
            "messaging_product": "whatsapp",
            "to": settings.CHANNEL_ID,
            "type": "text",
            "text": {"body": message},
        }
        try:
            response = requests.post(
                self.api_url, headers=self.headers, json=payload, timeout=10
            )
            response.raise_for_status()
            logger.info(f"Message sent successfully: {message}")
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(
                f"HTTP error: {e} - Response: {getattr(e.response, 'text', None)}"
            )
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
        return None
