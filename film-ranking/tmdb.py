import requests

api_key = "1e299e987b21695fb2938385baaf2224"
api_url = "https://api.themoviedb.org/search/movie?api_key=1e299e987b21695fb2938385baaf2224"
api_head_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZTI5OWU5ODdiMjE2OTVmYjI5MzgzODViYWFmMjIyNCIsInN1YiI6IjYxZDM2YzQyOTQ0YTU3MDAxZjhjNDM1OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vOFUt074Fnf1yl8dCPA3CQPq4QSEFCuRTjfVJk7PkbE"


def search_movie(title):
    response = requests.get(
        url="https://api.themoviedb.org/3/search/movie",
        params={"api_key": "1e299e987b21695fb2938385baaf2224",
                "query": title})

    response.raise_for_status()
    try:
        movie = response.json()["results"][0]
        my_movie = {
            "title": movie["title"],
            "year": movie["release_date"].split('-')[0],
            "description": movie["overview"],
            "rating": movie["vote_average"],
            "ranking": int(movie["popularity"]),
            "review": movie["title"],
            "img_url": "https://image.tmdb.org/t/p/original/" + movie["poster_path"],
        }
    except Exception:
        my_movie = None

    return my_movie

