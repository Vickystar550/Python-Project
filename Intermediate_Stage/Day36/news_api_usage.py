import requests

# making a get request to the news api

url = ('https://newsapi.org/v2/everything?'
       'q=Microsoft&'
       'from=2024-02-10&'
       'sortBy=popularity&'
       'apiKey=Enter Your Token Key Here')

response = requests.get(url)
response.raise_for_status()
data = response.json()

print(data)

