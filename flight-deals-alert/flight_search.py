import requests

endpoint = "https://tequila-api.kiwi.com/v2/search"
headers = {
    "apikey": "m2e9tqlsDAlN4fNs0Yd13IScxOLAd5V_",
}


class FlightSearch:
    def __int__(self):
        super().__init__()

    def get_search_parameters(self, fly_to, date_from, date_to):
        return {
            "fly_from": "ORD",
            "fly_to": fly_to,
            "dateFrom": date_from,
            "dateTo": date_to,
        }

    def search_flight(self, fly_to, date_from, date_to):
        parameters = self.get_search_parameters(fly_to, date_from, date_to)
        response = requests.get(url=endpoint, params=parameters, headers=headers)
        response.raise_for_status()
        print(response.json())
        return response.json()


FlightSearch().search_flight(fly_to="ORY", date_from="25/12/2021", date_to="01/04/2022")
