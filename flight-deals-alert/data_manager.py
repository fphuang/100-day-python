import requests
import datetime


class DataManager:

    def __int__(self):
        super().__init__()
        self.url = "https://api.sheety.co/6e7aecc5360db9e878b48c2a90e8a369/flightDeals/prices"
        self.headers = {"Authorization": "Bearer asdfaskjdfasjewrerekrjeljreljreljrljlejrelrjeljrererer"}

    def retrieve_sheet(self):
        # url = self.url
        # headers = self.headers
        response = requests.get("https://api.sheety.co/6e7aecc5360db9e878b48c2a90e8a369/flightDeals/prices", headers={"Authorization": "Bearer asdfaskjdfasjewrerekrjeljreljreljrljlejrelrjeljrererer"})
        response.raise_for_status()
        print(response.json())

    def put_sheet(self):
        date = datetime.datetime(year=2021, month=12, day=25)
        workout = {
            "prices": {
                "city": date.strftime("%m/%d/%Y"),
                "iataCode": "17:30:00",
                "lowestPrice": 180,
            }
        }
        response = requests.put(url=self.url, json=workout, headers=self.headers)
        response.raise_for_status()
        print(response.json())


DataManager().retrieve_sheet()