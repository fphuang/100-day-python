import requests
import datetime

APP_ID = "2497f9c6"
APP_KEY = "af27b4b01b8ab3f172fa9a73f25317ff"
URL = "trackapi.nutritionix.com/v2"


def query_nutrition():
    exercises = input("Tell me which exercises you did. ")
    parameters = {
        "query": exercises,
        "gender": "female",
        "weight_kg": 70,
        "height_cm": 175,
        "age": 30
    }
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "Content-Type": "application/json",
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                             json=parameters, headers=headers)
    response.raise_for_status()
    print(response.text)


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
