import requests


class Post:
    def __init__(self):
        self.url = 'https://api.npoint.io/c790b4d5cab58020d391'

    def get_posts(self):
        response = requests.get(url=self.url)
        response.raise_for_status()
        return response.json()