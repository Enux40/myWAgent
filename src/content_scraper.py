import requests
from bs4 import BeautifulSoup
import time
from config.sources import SOURCES
from src.logger import logger

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def fetch_html(url):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.warning(f"Attempt {attempt} failed for {url}: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"Failed to fetch {url} after {MAX_RETRIES} attempts.")
    return None


def scrape_techcrunch():
    source = next(s for s in SOURCES if s["name"] == "TechCrunch")
    html = fetch_html(source["url"])
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for article in soup.select(source["article_selector"]):
        try:
            headline_tag = article.select_one(source["headline_selector"])
            url_tag = article.select_one(source["url_selector"])
            date_tag = article.select_one(source["date_selector"])
            headline = headline_tag.get_text(strip=True) if headline_tag else None
            url = url_tag["href"] if url_tag and url_tag.has_attr("href") else None
            date = (
                date_tag["datetime"]
                if date_tag and date_tag.has_attr("datetime")
                else None
            )
            if headline and url:
                articles.append(
                    {
                        "headline": headline,
                        "url": url,
                        "date": date,
                    }
                )
        except Exception as e:
            logger.warning(f"Error parsing TechCrunch article: {e}")
    return articles


def scrape_theverge():
    source = next(s for s in SOURCES if s["name"] == "The Verge")
    html = fetch_html(source["url"])
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for article in soup.select(source["article_selector"]):
        try:
            headline_tag = article.select_one(source["headline_selector"])
            url_tag = article.select_one(source["url_selector"])
            date_tag = article.select_one(source["date_selector"])
            headline = headline_tag.get_text(strip=True) if headline_tag else None
            url = url_tag["href"] if url_tag and url_tag.has_attr("href") else None
            date = (
                date_tag["datetime"]
                if date_tag and date_tag.has_attr("datetime")
                else None
            )
            if headline and url:
                articles.append(
                    {
                        "headline": headline,
                        "url": url,
                        "date": date,
                    }
                )
        except Exception as e:
            logger.warning(f"Error parsing The Verge article: {e}")
    return articles


def scrape_mit_tech_review():
    source = next(s for s in SOURCES if s["name"] == "MIT Technology Review")
    html = fetch_html(source["url"])
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    for article in soup.select(source["article_selector"]):
        try:
            headline_tag = article.select_one(source["headline_selector"])
            url_tag = article.select_one(source["url_selector"])
            date_tag = article.select_one(source["date_selector"])
            headline = headline_tag.get_text(strip=True) if headline_tag else None
            url = url_tag["href"] if url_tag and url_tag.has_attr("href") else None
            date = (
                date_tag["datetime"]
                if date_tag and date_tag.has_attr("datetime")
                else None
            )
            if headline and url:
                articles.append(
                    {
                        "headline": headline,
                        "url": url,
                        "date": date,
                    }
                )
        except Exception as e:
            logger.warning(f"Error parsing MIT Technology Review article: {e}")
    return articles


def scrape_all_sources():
    return {
        "TechCrunch": scrape_techcrunch(),
        "The Verge": scrape_theverge(),
        "MIT Technology Review": scrape_mit_tech_review(),
    }


if __name__ == "__main__":
    all_articles = scrape_all_sources()
    for source, articles in all_articles.items():
        print(f"\nSource: {source}")
        for article in articles[:5]:  # Show only first 5 articles per source
            print(f"- {article['headline']} ({article['date']})\n  {article['url']}")
