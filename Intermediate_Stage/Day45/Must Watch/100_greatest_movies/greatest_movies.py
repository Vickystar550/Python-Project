import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

r = requests.get(url=URL)
movie_webpage = r.text

# with open('100_must_watch_webpage.html', 'w') as file:
#     file.write(BeautifulSoup(movie_webpage, "html.parser").prettify())

soup = BeautifulSoup(movie_webpage, 'html.parser')

movies = [movie.getText() for movie in soup.find_all(name='h3', class_='title')]

with open("100_greatest_movies.txt", 'w') as file:
    for m in movies[::-1]:
        print(m)
        file.write(f'{m}\n')

