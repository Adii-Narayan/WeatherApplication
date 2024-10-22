# weatherapp/weather/models.py

from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
