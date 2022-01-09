from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in all_movies[::-1]]

with open(file='movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
