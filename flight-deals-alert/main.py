import requests
import datetime

url_sheet = "https://api.sheety.co/6e7aecc5360db9e878b48c2a90e8a369/myWorkouts/workouts"
BEARER_TOKEN = "asdfaskjdfasjewrerekrjeljreljreljrljlejrelrjeljrererer"
HEADERS = {"Authorization": f"Bearer {BEARER_TOKEN}"}

def retrieve_sheet():
    response = requests.get(url=url_sheet, headers=HEADERS)
    response.raise_for_status()
    print(response.json())


# retrieve_sheet()


def post_sheet():
    date = datetime.datetime(year=2021, month=12, day=25)
    workout = {
        "workout": {
            "date": date.strftime("%m/%d/%Y"),
            "time": "17:30:00",
            "duration": 180,
            "exercise": "walk".title(),
            "calories": 800,
        }
    }
    response = requests.post(url=url_sheet, json=workout, headers=HEADERS)
    response.raise_for_status()
    print(response.json())


post_sheet()




#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.