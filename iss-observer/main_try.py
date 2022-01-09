import requests

def request_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = data["iss_position"]['longitude']
    latitude = data["iss_position"]['latitude']


def get_kanye_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    print(data['quote'])


