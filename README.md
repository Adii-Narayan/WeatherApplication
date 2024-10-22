# Weather App

A simple weather application built using Django, which allows users to fetch real-time weather information based on city names. The application utilizes the OpenWeatherMap API to retrieve weather data and stores previously fetched data in the session.

## Features

- Fetches current weather data for a specified city.
- Displays temperature, weather description, and an icon representing the weather.
- Stores fetched weather data in the session, allowing for retrieval until the page is refreshed.
- Responsive design with a visually appealing layout.

## Technologies Used

- Python
- Django
- HTML/CSS
- JavaScript
- OpenWeatherMap API

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Django 5.x
- Requests library

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd weatherapp
2.Install the required packages:
     pip install django requests
3.Set the OpenWeatherMap API Key:

Replace the placeholder in views.py with your actual API key.
API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key

4.Database Migrations
Make migrations:
    python manage.py makemigrations
Apply migrations:
    python manage.py migrate
5.Running the Server
	python manage.py runserver
