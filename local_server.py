import sys
from mcp.server.fastmcp import FastMCP

from services.weather_service import WeatherService
from services.news_service import NewsService
from services.currency_service import CurrencyService


print("Запуск сервера...", file=sys.stderr)

try:
    # Инициализация сервера и сервисов
    mcp = FastMCP("info-services")
    weather_service = WeatherService()
    news_service = NewsService()
    currency_service = CurrencyService()

    @mcp.tool()
    async def get_weather(city: str) -> str:
        """Получить прогноз погоды для города

        Args:
            city: Название города
        """
        print(f"Получен запрос погоды для города: {city}", file=sys.stderr)
        return weather_service.get_current_weather(city)

    @mcp.tool()
    async def get_news(count: int = 5) -> str:
        """Получить топ новостей

        Args:
            count: Количество новостей для отображения (по умолчанию 5)
        """
        print(f"Получен запрос на {count} новостей", file=sys.stderr)
        return news_service.get_top_news(count)

    @mcp.tool()
    async def get_dollar_rate() -> str:
        """Получить текущий курс доллара"""
        print("Получен запрос курса доллара", file=sys.stderr)
        return currency_service.get_dollar_rate()

    if __name__ == "__main__":
        print("Сервер готов к работе", file=sys.stderr)
        mcp.run()
except Exception as e:
    print(f"Ошибка при запуске сервера: {e}", file=sys.stderr)
    raise
