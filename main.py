from src.whatsapp_api import WhatsAppAPI
from src.logger import logger

if __name__ == "__main__":
    wa_api = WhatsAppAPI()
    test_message = "This is a test message from the WhatsApp AI Agent."
    logger.info("Sending test message...")
    result = wa_api.send_message(test_message)
    if result:
        logger.info(f"API Response: {result}")
    else:
        logger.error("Failed to send test message.")
