#!/usr/bin/env python3

#  This will be a weather app for Huntsville, AL.

# Imports
import requests

# Variables
api_key = '8f6290cb43c8e84d428d161d9199c45b '
city = input ('Enter city name: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Tempature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
