# List of tech news sources and their scraping selectors

SOURCES = [
    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/",
        "article_selector": "article.post-block",
        "headline_selector": "h2.post-block__title a",
        "url_selector": "h2.post-block__title a",
        "date_selector": "time",
    },
    {
        "name": "The Verge",
        "url": "https://www.theverge.com/tech",
        "article_selector": "div.c-compact-river__entry",
        "headline_selector": "h2.c-entry-box--compact__title a",
        "url_selector": "h2.c-entry-box--compact__title a",
        "date_selector": "time",
    },
    {
        "name": "MIT Technology Review",
        "url": "https://www.technologyreview.com/",
        "article_selector": "div.stream-article",
        "headline_selector": "a.stream-article__title",
        "url_selector": "a.stream-article__title",
        "date_selector": "time",
    },
]
