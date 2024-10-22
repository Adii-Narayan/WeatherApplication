# weatherapp/weather/tasks.py

from background_task import background
from .models import WeatherData  # Assuming you have a model to store weather data
import requests

API_KEY = 'd689d82d5bc1e814e6e81401975b6989'  # Use your actual API key

@background(schedule=300)  # Schedule to run every 5 minutes (300 seconds)
def fetch_weather(city):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        # Here you might want to save the weather data to your database
        # For example:
        WeatherData.objects.update_or_create(
            city=city,
            defaults={
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        )
    else:
        print(f"Error fetching weather data for {city}: {data.get('message', 'Unknown error')}")
