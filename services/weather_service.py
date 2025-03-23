import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("ACCUWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("ACCUWEATHER_API_KEY в файле .env не найден")

    def get_location_key(self, city_name: str) -> str | None:
        """Получает LocationKey для заданного города."""
        location_url = "https://dataservice.accuweather.com/locations/v1/cities/search"
        params = {
            "apikey": self.api_key,
            "q": city_name,
            "language": "ru-ru",
            "offset": 1,
        }

        try:
            response = requests.get(location_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data[0]["Key"] if data else None
        except Exception as e:
            print(f"Ошибка при получении LocationKey: {e}")
            return None

    def get_current_weather(self, city: str) -> str:
        """Получает текущую погоду для города."""
        try:
            location_key = self.get_location_key(city)
            if not location_key:
                return f"Не удалось найти город {city}"

            weather_url = f"https://dataservice.accuweather.com/currentconditions/v1/{location_key}"
            params = {"apikey": self.api_key, "language": "ru-ru"}

            response = requests.get(weather_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data:
                weather = data[0]
                return f"Погода в городе {city}: {weather['WeatherText']}, {weather['Temperature']['Metric']['Value']}°C"
            else:
                return f"Данные о погоде для города {city} не найдены"
        except Exception as e:
            return f"Ошибка при получении погоды: {e}"
