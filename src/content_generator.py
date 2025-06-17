import os
import hashlib
import requests
from src.logger import logger
from config import settings

# Store hashes of processed articles to avoid duplicates (in-memory for now)
PROCESSED_HASHES = set()

OPENAI_API_URL = os.getenv(
    "OPENAI_API_URL", "https://api.openai.com/v1/chat/completions"
)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    logger.error(
        "OPENAI_API_KEY environment variable is required for content generation."
    )

LLM_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

PROMPT_TEMPLATE = (
    "You are an expert tech news summarizer. Given the following article, generate a concise, factual, and engaging summary (150-300 characters) suitable for a WhatsApp channel update. "
    "Highlight the core innovation and its potential impact. Use clear, simple language, avoid jargon or explain it simply, and optimize for mobile readability. "
    "Start or end with a relevant emoji. Add a 'Why it matters:' takeaway. Do not include the article URL in the summary.\n\n"
    "Article:\n{article_text}\n"
    "Summary:"
)


def is_relevant_article(headline, article_text):
    # Simple filter: must mention tech/innovation keywords
    keywords = [
        "AI",
        "technology",
        "innovation",
        "startup",
        "robot",
        "software",
        "hardware",
        "science",
        "research",
        "launch",
        "product",
        "platform",
    ]
    text = f"{headline} {article_text}".lower()
    return any(kw.lower() in text for kw in keywords)


def hash_article(url, title):
    return hashlib.sha256(f"{url}|{title}".encode("utf-8")).hexdigest()


def is_duplicate(url, title):
    h = hash_article(url, title)
    if h in PROCESSED_HASHES:
        return True
    PROCESSED_HASHES.add(h)
    return False


def generate_summary(article_text):
    if not OPENAI_API_KEY:
        logger.error("No OpenAI API key set. Skipping summarization.")
        return None
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": PROMPT_TEMPLATE.format(article_text=article_text),
            },
        ],
        "max_tokens": 200,
        "temperature": 0.7,
    }
    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=data, timeout=20)
        response.raise_for_status()
        result = response.json()
        summary = result["choices"][0]["message"]["content"].strip()
        return summary
    except Exception as e:
        logger.error(f"LLM summarization failed: {e}")
        return None


def format_summary(summary, url):
    return f"{summary}\nRead more: {url}"
