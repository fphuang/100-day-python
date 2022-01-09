import requests
from datetime import datetime

TOKEN = "hajaflajdf3343434kjkjkk"
USER_NAME = "fp"

user_end_point = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": 'yes'
}


def create_user():
    response = requests.post(url=user_end_point, json=user_params)
    response.raise_for_status()
    print(response.text)

# create_user()

GRAPH_ID = "graph-soccer"
graph_endpoint = f"{user_end_point}/{USER_NAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "soccer",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}
graph_headers = {
    "X-USER-TOKEN": TOKEN
}


def create_graph():
    response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
    response.raise_for_status()
    print(response.text)


graph_update_endpoint =  f"{user_end_point}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime(year=2021,month=12,day=23)
update_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

graph_update_endpoint =  f"{user_end_point}/{USER_NAME}/graphs/{GRAPH_ID}"

def report_activity():
    response = requests.post(url=graph_update_endpoint, json=update_params, headers=graph_headers)
    response.raise_for_status()
    print(response.text)


# report_activity()

update_params = {
    "date": today.strftime("%Y%m%d"),
}

body = {
    "quantity": "4",
}

date = datetime(year=2021, month=12, day=23).strftime("%Y%m%d")
graph_update_endpoint = f"{user_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"

def update_activity():
    response = requests.put(url=graph_update_endpoint, json=body, headers=graph_headers)
    response.raise_for_status()
    print(response.text)



def delete_activity():
    date = datetime(year=2021, month=12, day=23).strftime("%Y%m%d")
    endpoint = f"{user_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(url=endpoint, headers=graph_headers)
    response.raise_for_status()
    print(response.text)

delete_activity()
