from django.urls import path
from .views import index, clear_weather_data

urlpatterns = [
    path('', index, name='index'),
    path('clear-weather-data/', clear_weather_data, name='clear_weather_data'),
]
