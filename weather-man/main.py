import requests
import os
from twilio.rest import Client

api_key = os.environ.get("api_key")

phone_number = os.environ.get("phone_number")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

print(phone_number)


parameters = {
    'lat': 3.073930,
    "lon": -89.385240,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
url = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="it is going to rain.",
        from_=phone_number,
        to='+12165517819'
    )

    print(message.status)
