import requests

url = "https://api.themoviedb.org/3/movie/603?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMDhlMzA2MGQ3ZWY4ZWFkOGZjM2ViNGRjZWRlMjk4ZiIsInN1YiI6IjY1ZGU2NzcyM2ZmMmRmMDE4NzBiZDVhNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z5pjHhtbitAfjv5vKlge-OGgxJtj6gzktnB3WPp-W8Y"
}

response = requests.get(url, headers=headers)

print(response.text)

print(response.json())
