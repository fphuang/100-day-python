import requests


def load_questions():
    url = "https://opentdb.com/api.php"
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()["results"]
