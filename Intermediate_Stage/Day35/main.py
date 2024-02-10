import requests

# ------------- Etinan
lat = 4.847800
lon = 7.850800

parameters = {
    "lat": 6.6009,
    "lon": 3.4882,
    "appid": "Enter your API key"
}

url = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)




