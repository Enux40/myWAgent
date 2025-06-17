import os
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from config import settings
from src.content_scraper import scrape_all_sources
from src.content_generator import (
    is_relevant_article,
    is_duplicate,
    generate_summary,
)
from src.whatsapp_api import WhatsAppAPI
from src.whatsapp_poster import post_to_channel, format_channel_message
from src.logger import logger

# Configurable number of articles to post daily
N_TOP_ARTICLES = int(os.getenv("N_TOP_ARTICLES", 2))
POST_TIME = settings.DEFAULT_POST_TIME  # e.g., '09:00'

wa_api = WhatsAppAPI()


def run_daily_update():
    logger.info("Starting daily update process...")
    all_articles = scrape_all_sources()
    selected = []
    # Flatten and filter articles
    for source, articles in all_articles.items():
        for article in articles:
            if not article.get("headline") or not article.get("url"):
                continue
            article_text = article["headline"]  # Placeholder for full text
            if not is_relevant_article(article["headline"], article_text):
                continue
            if is_duplicate(article["url"], article["headline"]):
                continue
            selected.append(
                {
                    "headline": article["headline"],
                    "url": article["url"],
                    "date": article.get("date"),
                    "source": source,
                    "text": article_text,
                }
            )
    # Prioritize (by date, fallback to order)
    selected = sorted(selected, key=lambda x: x["date"] or "", reverse=True)[
        :N_TOP_ARTICLES
    ]
    for article in selected:
        logger.info(f"Generating summary for: {article['headline']}")
        summary = generate_summary(article["text"])
        if not summary:
            logger.warning(f"No summary generated for: {article['headline']}")
            continue
        # Extract 'Why it matters' from summary if present, else fallback
        why_matters = "See the article for details."
        if "Why it matters:" in summary:
            parts = summary.split("Why it matters:", 1)
            summary_text = parts[0].strip()
            why_matters = parts[1].strip()
        else:
            summary_text = summary
        message = format_channel_message(
            article["headline"], summary_text, why_matters, article["url"]
        )
        logger.info(f"Posting to WhatsApp Channel: {message}")
        post_to_channel(settings.CHANNEL_ID, message)
    logger.info("Daily update process complete.")


def schedule_daily():
    scheduler = BackgroundScheduler()
    hour, minute = map(int, POST_TIME.split(":"))
    scheduler.add_job(run_daily_update, "cron", hour=hour, minute=minute)
    scheduler.start()
    logger.info(f"Scheduled daily update at {POST_TIME}.")
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")


if __name__ == "__main__":
    schedule_daily()
