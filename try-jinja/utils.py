import requests


def guess_gender(name):
    response = requests.get(url="https://api.genderize.io", params={"name": name})
    response.raise_for_status()
    return response.json()["gender"]


def guess_age(name):
    response = requests.get(url="https://api.agify.io", params={"name": name})
    response.raise_for_status()
    return response.json()["age"]


def get_blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    return response.json()


if __name__ == '__main__':
    print(get_blog())