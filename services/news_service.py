import os
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv

load_dotenv()


class NewsService:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = os.getenv("NEWS_API_BASE_URL")
        if not self.api_key or not self.base_url:
            raise ValueError(
                "NEWS_API_KEY или NEWS_API_BASE_URL не найдены в файле .env"
            )

    def get_top_news(self, count: int = 5) -> str:
        """Получает топ новостей."""
        try:
            # Получаем даты для запроса (последние 7 дней)
            today = datetime.now()
            week_ago = today - timedelta(days=7)

            params = {
                "sources": "lenta",
                "from": week_ago.strftime("%Y-%m-%d"),
                "to": today.strftime("%Y-%m-%d"),
                "language": "ru",
                "apiKey": self.api_key,
            }

            response = requests.get(f"{self.base_url}/top-headlines", params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("articles"):
                news_list = data["articles"][:count]
                result = "Топ новостей:\n\n"
                for i, article in enumerate(news_list, 1):
                    result += f"{i}. {article['title']}\n"
                    if article.get("description"):
                        result += f"{article['description']}\n"
                    result += f"Подробнее: {article['url']}\n\n"
                return result
            else:
                return "Новости не найдены"
        except Exception as e:
            return f"Ошибка при получении новостей: {e}"
