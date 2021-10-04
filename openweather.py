# Python program adapted to find current weather details of any city
# Program using API to get weather information from cities
# using openweathermap api, go to https://openweathermap.org/ to details

# Importing libraries required
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

# Enter your API key here
API_KEY = os.getenv("API_KEY")


# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
cities = ["Vancouver"]

for site in cities:

    #city_name = input("Enter city name : ")

    # complete_url variable to store
    # complete url address

    complete_url = base_url + "appid=" + API_KEY + "&q=" + site

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x['main']

        # store the value corresponding
        # to the "temp" key of y
        current_t = y["temp"]
        current_temperature = current_t - 273.15
        current_temp_float = "{:.2f}".format(current_temperature)

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # store the value corresponding
        # to the "country_code"
        country_code = x['sys']['country']

        # print following values
        print(site)
        print(" Temperature (in kelvin unit) = " +
              str(current_temp_float) +
              "\n Atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n Mumidity (in percentage) = " +
              str(current_humidity) +
              "\n Description = " +
              str(weather_description) +
              "\n Country code = " + str(country_code))
    else:
        print(" City Not Found ")
