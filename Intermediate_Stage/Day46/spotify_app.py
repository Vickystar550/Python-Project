from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
import requests
from bs4 import BeautifulSoup

# ################### Scraping BILLBOARD 100 ################
travel_back = input("What year do you want to travel back to. Please type it in this format YYYY-MM-DD\n")

URL = f"https://www.billboard.com/charts/hot-100/{travel_back}/"
r = requests.get(url=URL)

soup = BeautifulSoup(r.text, 'html.parser')
songs = [s.getText().strip() for s in soup.select('li ul li h3')]
print(songs)

# ##################### SPOTIFY #########################
CLIENT_ID = "enter here"
CLIENT_SECRET = "enter here"
REDIRECTED_URL = "https://github.com/Vickystar550"
REFRESH_TOKEN = "enter here"
# spotify authentication:
oauth_manager = SpotifyOAuth(client_id=CLIENT_ID,
                             client_secret=CLIENT_SECRET,
                             redirect_uri=REDIRECTED_URL,
                             scope="playlist-modify-private",
                             cache_path="token.txt")
x = oauth_manager.refresh_access_token(refresh_token=REFRESH_TOKEN)
print(x)

sp = Spotify(oauth_manager=oauth_manager)

user_id = sp.current_user()['id']

# getting song item identification string:
year = travel_back.split("-")[0]
songs_uri = []
for song in songs:
    r = sp.search(q=f"track: {song} year {year}", type='track')
    try:
        uri = r["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(songs_uri)

# create a playlist
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{travel_back} Billboard 100",
                                   public=False,
                                   collaborative=False,
                                   description=f'playlist for 100 trending track on {travel_back}')

print(playlist)

# add song items to playlist
sp.playlist_add_items(playlist_id=playlist.get('id'),
                      items=songs_uri,
                      )
print(playlist)
