import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    def __init__(self) -> None:
        self.api_key: str = os.getenv("WEATHER_API_KEY", "demo_key")
        self.api_url: str = os.getenv("WEATHER_API_URL", "https://api.openweathermap.org/data/2.5/weather")

    def obtener_clima_mendoza(self) -> Dict[str, Any]:
        """Consulta el clima o retorna un fallback de prueba."""
        params = {
            "q": "Mendoza,AR",
            "appid": self.api_key,
            "units": "metric",
            "lang": "es"
        }
        try:
            response = requests.get(self.api_url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {
                    "temp": data["main"]["temp"],
                    "descripcion": data["weather"][0]["description"]
                }
            return {"temp": 22.0, "descripcion": "cielo despejado (simulado)"}
        except Exception:
            return {"temp": 20.0, "descripcion": "parcialmente nublado (fallback)"}