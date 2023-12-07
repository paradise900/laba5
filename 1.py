import json
import requests
from kinopoisk_dev import KinopoiskDev # pip install kinopoisk-dev


def weather_conditions():
    city_name = input('Enter city: ')
    key = '8d34fc01f773e6e8e79e6b4e39b79ee5'
    response = requests.post(f'http://api.openweathermap.org/data/2.5/weather?q={city_name},&APPID={key}')
    result = json.loads(response.text)
    print(f'So, the weather in {city_name}: {result["weather"][0]["description"]}')
    print(f'Temperature: {result["main"]["temp"]} deg')
    print(f"Pressure: {result['main']['pressure']} pa")
    print(f"Humidity: {result['main']['humidity']}%")


def kinopoisk():
    TOKEN = 'HH2KBFB-KYHMR51-HVP0TSS-B7QRB8V'
    kp = KinopoiskDev(token=TOKEN)
    return kp.random()


print('Weather conditions')
weather_conditions()
print('\n')
data = kinopoisk()
print('Kinopoisk')
print(f'Name: {data.name}')
print(f'Description: {data.description}')
print(f'Slogan: {data.slogan}')
print(f'Raiting kinopoisk: {data.rating.kp}, imdb: {data.rating.imdb}, tmdb: {data.rating.tmdb}')
print(f'Movie lenght: {data.movieLength}')
print(f'Age raiting: {data.ageRating}')
