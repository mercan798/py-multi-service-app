from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

def get_weather(city):
    if not city:
        return "Please provide a city name."
    if not OPEN_WEATHER_API_KEY:
        return "OpenWeather API key not configured."
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPEN_WEATHER_API_KEY, "units": "metric"}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        temperature = data.get("main", {}).get("temp")
        description = data.get("weather", [{}])[0].get("description", "no description")
        if temperature is None:
            return "Weather data unavailable for that city."
        return f"The temperature in {city} is {temperature}°C with {description}."
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather: {e}"
