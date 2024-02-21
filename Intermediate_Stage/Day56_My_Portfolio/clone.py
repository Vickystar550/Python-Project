import requests
from bs4 import BeautifulSoup
import lxml

r = requests.get(url='https://html5up.net/astral')
r.text

soup = BeautifulSoup(r.text, 'lxml')

# print(soup.prettify())


tweet = soup.select_one(selector='//*[@id="nav"]/a[4]')
print(tweet)
