import requests
from bs4 import BeautifulSoup

travel_back = input("What year do you want to travel back to. Please type it in this format YYYY-MM-DD\n")

URL = f"https://www.billboard.com/charts/hot-100/{travel_back}/"

r = requests.get(url=URL)

soup = BeautifulSoup(r.text, 'html.parser')

songs = [s.getText().strip() for s in soup.select('li ul li h3')]
print(songs)

# getting the corresponding artists:
song_owners = soup.select('li ul li span')
cleaned_owners_list = [a.getText().strip() for a in song_owners]

artists = [a for a in cleaned_owners_list if not (a == '-' or a.isnumeric())]


rank = 0
with open("billboard.txt", 'w') as file:
    for song, artist in zip(songs, artists):
        rank += 1
        file.write(f'SONG:\t{song}\nARTIST(s):\t{artist}\nRANK:\t{rank}\n\n')

        print(f'SONG:\t{song}')
        print(f'ARTIST(s):\t{artist}')
        print(f'RANK:\t{rank}\n')


