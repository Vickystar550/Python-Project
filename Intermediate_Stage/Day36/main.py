"""This program make a get request the newsapi and saves the result to a json file"""

import requests
import json

url = ('https://newsapi.org/v2/everything?'
       'q="Tesla Inc"&'
       'from=2024-02-10&'
       'sortBy=popularity&'
       'apiKey=Enter Your Token Key Here')
response = requests.get(url)
data = response.json()

with open("data.json", mode="w") as file:
    json.dump(data, file, indent=4)
