from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

API_KEY = 'd689d82d5bc1e814e6e81401975b6989'  

def index(request):
    weather_data = request.session.get('weather_data', {})  # Get weather data from session

    if request.method == 'GET':
        city = request.GET.get('city')  # Get the city from the query parameters
        if city:
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
                request.session['weather_data'] = weather_data  # Store weather data in session
            else:
                weather_data = {'error': 'City not found!'}
                request.session['weather_data'] = {}  # Clear session on error

    return render(request, 'index.html', {'weather_data': weather_data})
@csrf_exempt  # Use this for development; in production, use CSRF tokens properly
def clear_weather_data(request):
    if request.method == 'POST':
        if 'weather_data' in request.session:
            del request.session['weather_data']  # Clear the stored weather data
    return JsonResponse({'status': 'success'})