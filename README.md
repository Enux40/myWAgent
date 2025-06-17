# WhatsApp AI Agent: Automated Tech Innovation Updates

## Overview
This project is an autonomous AI agent that curates, summarizes, and posts daily technology innovation news updates to a designated WhatsApp Channel. It combines web scraping, AI-powered summarization, and automated scheduling to keep your audience informed with the latest in tech innovation.

## Features
- **Automated Web Scraping:** Fetches news from top tech sources (TechCrunch, The Verge, MIT Technology Review).
- **AI Summarization:** Uses an LLM (e.g., OpenAI GPT-4) to generate concise, engaging summaries optimized for WhatsApp.
- **Content Filtering & Deduplication:** Ensures only relevant, non-duplicate articles are posted.
- **WhatsApp Channel Integration:** Posts formatted updates directly to your WhatsApp Channel using the WhatsApp Business API.
- **Daily Scheduling:** Runs automatically at a configurable time each day.
- **Robust Logging & Error Handling:** All operations are logged for transparency and troubleshooting.

## Project Structure
```
myWA-agent/
├── config/              # Configuration files (API keys, sources, settings)
│   ├── settings.py
│   └── sources.py
├── logs/                # Log files
├── src/                 # Source code
│   ├── content_scraper.py      # Web scraping logic
│   ├── content_generator.py    # AI summarization and filtering
│   ├── logger.py               # Logging setup
│   ├── scheduler.py            # Scheduling and orchestration
│   ├── whatsapp_api.py         # WhatsApp API integration
│   └── whatsapp_poster.py      # WhatsApp channel posting and formatting
├── .env                 # Environment variables (not tracked in git)
├── .gitignore           # Git ignore rules
├── main.py              # Entry point for manual testing
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Setup Instructions
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Enux40/myWAgent.git
   cd myWAgent
   ```
2. **Create and Activate a Virtual Environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables:**
   - Copy `.env.example` to `.env` and fill in your WhatsApp API credentials and settings.
   - Never commit your real `.env` to a public repository.
5. **Run the Agent:**
   - For a one-time test:
     ```sh
     python main.py
     ```
   - To start the daily scheduler:
     ```sh
     python src/scheduler.py
     ```

## Environment Variables (.env)
```
WHATSAPP_API_TOKEN=your_whatsapp_api_token
WHATSAPP_CHANNEL_ID=your_channel_id
WHATSAPP_API_URL=https://graph.facebook.com/v19.0
LOG_FILE_PATH=logs/app.log
LOG_LEVEL=INFO
DEFAULT_POST_TIME=09:00
OPENAI_API_KEY=your_openai_api_key
```

## Security Notice
- **Never commit your `.env` file with real credentials to a public repository.**
- Use `.gitignore` to keep secrets out of version control.

## License
This project is for educational and demonstration purposes. Please review and comply with WhatsApp and OpenAI terms of service for production use.

---

For questions or contributions, open an issue or pull request on GitHub.
