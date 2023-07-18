

import requests
class WeatherAPI:

    def __init__(self, api_key):

        self.api_key = api_key

        self.base_url = 'https://api.weatherapi.com/v1'




    def get_weather(self, location):

        url = f'{self.base_url}/current.json?key={self.api_key}&q={location}'

        response = requests.get(url)

        data = response.json()




        if 'error' in data:

            print(f"Error: {data['error']['message']} \n")

        else:

            weather = data['current']

            print(f"\nWeather in {location}:")

            print(f"Temperature: {weather['temp_c']}°C")

            print(f"Condition: {weather['condition']['text']}")

            print(f"Wind Speed: {weather['wind_kph']} km/h")

            print(f"Humidity: {weather['humidity']}%\n")




# Usage

api_key = open("./api.txt", "r").read()  #API key

weather_api = WeatherAPI(api_key)

location = input("Enter the desired location to get weather information: \n")  #Your desired location

weather_api.get_weather(location)


