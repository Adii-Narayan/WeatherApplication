from django.contrib import admin
from django.urls import path
from weatherapp.weather import views  # Correct import from the weather app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Route to the index view
]
