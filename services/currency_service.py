import os
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

load_dotenv()

class CurrencyService:
    def __init__(self):
        self.api_url = os.getenv('CBR_API_URL')
        if not self.api_url:
            raise ValueError("CBR_API_URL not found in environment variables")

    def get_dollar_rate(self) -> str:
        """Получает текущий курс доллара."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            
            tree = ET.fromstring(response.content)
            for currency in tree.findall("Valute"):
                if currency.find("CharCode").text == "USD":
                    rate = currency.find("Value").text
                    return f"Курс доллара: {rate} руб."
            
            return "Курс доллара не найден"
        except Exception as e:
            return f"Ошибка при получении курса валют: {e}" 