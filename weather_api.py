from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

def get_weather(city):
    if not city or not str(city).strip():
        return "Please provide a city name."

    city = str(city).strip()

    if not OPEN_WEATHER_API_KEY:
        return "OpenWeather API key not configured. Please set OPEN_WEATHER_API_KEY in .env."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPEN_WEATHER_API_KEY, "units": "metric"}

    try:
        resp = requests.get(url, params=params, timeout=10)

        if resp.status_code == 404:
            return f"City '{city}' not found. Check spelling and try again."

        resp.raise_for_status()
        data = resp.json()

        main = data.get("main") or {}
        weather_list = data.get("weather") or []

        temperature = main.get("temp")
        feels_like = main.get("feels_like")
        humidity = main.get("humidity")
        description = weather_list[0].get("description") if weather_list else "No description"

        if temperature is None:
            return "Weather data unavailable for that city."

        result = f"Weather for {city}: {description.capitalize()}. Temperature: {temperature}°C"

        if feels_like is not None:
            result += f", feels like {feels_like}°C"

        if humidity is not None:
            result += f", humidity {humidity}%"

        return result

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather: {e}"
