import requests
import json
import matplotlib.pyplot as plt
import calendar
import base64
import io
import urllib

from io import StringIO
from datetime import datetime

apiKey = "80aef63b731dac4699efe44ff5ebfed3"

def convert_time_to_timezone(utc, tz_offset):
    time = utc + tz_offset
    time = datetime.utcfromtimestamp(time).strftime('%I:%M %p')
    return (time)

def convert_time_to_day(utc, tz_offset):
    time = utc + tz_offset
    day = datetime.utcfromtimestamp(time).strftime("%A")
    return day

# This function retrieves weather information using the OpenWeatherMap - One Call API to create a weather forecast using real time
def get_current_forecast(lat, lon):

    # These variables are used to make the API GET request call
    units = "imperial"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + apiKey + "&units=" + units 

    # Makes the API request
    response = requests.get(url)

    # Converts the JSON string created from the API call and converts it into a dictionary
    data = json.loads(response.content)
    
    current_weather = {
        'name': data['name'],
        'description': data['weather'][0]['description'].title(),
        'temp': str(round(data['main']['temp'])) + " °F",
        'temp_min': str(round(data['main']['temp_min'])) + " °F",
        'temp_max': str(round(data['main']['temp_max'])) + " °F",
        'wind': str(data['wind']['speed']) + " mph",
        'humidity': str(data['main']['humidity']) + " %",
        'pressure': str(data['main']['pressure']) + " hPa",
        'sunrise': convert_time_to_timezone(data['sys']['sunrise'], data['timezone']),
        'sunset': convert_time_to_timezone(data['sys']['sunset'], data['timezone']),
    }

    return (current_weather)


# This function retrieves weather information using the OpenWeatherMap - One Call API to create a weather forecast using real time
def get_weekly_forecast(lat, lon):

    # These variables are used to make the API GET request call
    units = "imperial"
    part = "current,minutely,hourly"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&units=" + units + "&exclude=" + part + "&appid=" + apiKey

    # Makes the API request
    response = requests.get(url)

    # Converts the JSON string created from the API call and converts it into a dictionary
    data = json.loads(response.content)

    day_of_week = []
    temp_max = []
    temp_min = []
    description = []
    today = True

    # Get the data for the 7-day forecast plot
    for day in data['daily']:

        if (today):
            today = False
            day_of_week.append("Today" + "\n" + day['weather'][0]['description'].title())
        else:
            day_of_week.append(convert_time_to_day(day['dt'], data['timezone_offset']) + "\n" +  day['weather'][0]['description'].title())
            
        temp_max.append(day['temp']['max'])
        temp_min.append(day['temp']['min'])
        description.append(day['weather'][0]['description'].title())

    plt.figure(figsize=(12,4))
    plt.plot(day_of_week, temp_max, label = "Highs")
    plt.plot(day_of_week, temp_min, label = "Lows")
    plt.xlabel('Day of the Week')
    plt.ylabel('Temperature (°F)')
    plt.title('7-Day Forecast')
    plt.legend()

    flike = io.BytesIO()
    plt.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
        
    return b64
    


# # The code to run
# def main():
#     lat = "40.7128"
#     lon = "-74.0060"
#     result = get_weekly_forecast(lat, lon)
#     # result.show()

#     # result = get_current_forecast(lat, lon)
#     # print(result)

# main()