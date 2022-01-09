import requests
import datetime

MY_LAT = 36.7201600
MY_LNG = -4.4203400

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

print(sunset_hour)
print(sunrise_hour)

time_now = datetime.datetime.now()
print(time_now.hour)