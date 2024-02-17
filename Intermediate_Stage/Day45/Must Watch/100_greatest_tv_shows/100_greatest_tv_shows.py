import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200611015421/https://www.empireonline.com/movies/features/best-tv-shows-ever-2/"

r = requests.get(url=URL)

soup = BeautifulSoup(r.text, "html.parser")

shows = [show.getText() for show in soup.find_all(name='h3', class_='title')][::-1]

clean_list = [s if s.find(")") == -1 else s[s.find(")") + 2:] for s in shows]

with open('100_greatest_tv_shows.txt', 'w') as file:
    for index, title in enumerate(clean_list, start=1):
        print(f'{index}\t{title}')
        file.write(f'{index}\t{title}\n')
