from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

spotify_user_name = "31axcp4brsojmbpg5aqdyn2vl3ae"
spotify_client_id = "30fce1383dda49189c9d75318f33cb91"
spotify_client_secret = "978fd0f1892d4d06a58b5bf329a02c07"

sp = spotipy.Spotify(auth_manager=
                     SpotifyOAuth(scope="playlist-modify-private user-library-read",
                                  client_id=spotify_client_id,
                                  redirect_uri="http://example.com",
                                  client_secret=spotify_client_secret,
                                  show_dialog=True,
                                  cache_path="token.txt"))

user_id = sp.current_user()["id"]

with open('top-100-2013-12-31.txt') as file:
    song_names = file.read().split('\n')

song_uris = []
year = "2013"
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

half_count = len(song_uris)//2
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard Top 100 - Part 1", public=False,
                                   description="created by Python")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris[:half_count])

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard Top 100 - Part 2", public=False,
                                   description="created by Python")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris[half_count:])
