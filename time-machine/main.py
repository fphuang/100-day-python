from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

the_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{the_date}"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{the_date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
songs_data = soup.find_all(name="h3", id="title-of-a-story")
songs = []
for song_raw in songs_data:
    song = song_raw.getText()
    if "\nSongwriter(s):\n" not in song and "\nProducer(s):\n" not in song:
        if "\nImprint/Promotion Label:\n" not in song:
            if "Is Australia's Christmas No. 1\n\n" not in song:
                if "\nGains in Weekly Performance\n" not in song:
                    if "\nAdditional Awards\n" not in song:
                        songs.append(song.strip().lower())


with open(f'top-100-{the_date}.txt', 'w') as file:
    for n in range(len(songs)):
        song = songs[n]
        file.write(f"{song}\n")
