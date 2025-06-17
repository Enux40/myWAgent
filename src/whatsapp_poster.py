from config import settings
import requests
from src.logger import logger

WHATSAPP_API_URL = settings.API_URL
API_TOKEN = settings.API_TOKEN


def post_to_channel(channel_id, message_content):
    url = f"{WHATSAPP_API_URL}/{channel_id}/messages"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": channel_id,
        "type": "text",
        "text": {"body": message_content},
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Message posted to channel {channel_id} successfully.")
        return response.json()
    except requests.exceptions.HTTPError as e:
        logger.error(
            f"HTTP error posting to channel: {e} - Response: {getattr(e.response, 'text', None)}"
        )
        if e.response is not None and e.response.status_code == 400:
            logger.error("Possible invalid channel ID or message format.")
        elif e.response is not None and e.response.status_code == 413:
            logger.error("Message size limit exceeded for WhatsApp channel.")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error posting to channel: {e}")
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout error posting to channel: {e}")
    except Exception as e:
        logger.error(f"Unexpected error posting to channel: {e}")
    return None


def format_channel_message(headline, summary, why_matters, url):
    # WhatsApp supports some Markdown-like formatting (bold, italics, monospace)
    return (
        f"*{headline}*\n{summary}\n_Why it matters:_ {why_matters}\n[Read More]({url})"
    )
