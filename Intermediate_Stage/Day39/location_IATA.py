import requests
import json

SHEETY_TOKEN = "Enter your api key here"
TEQUILLA_FLIGHT_API_TOKEN = "Your api key here"


with open("sheety_data.json", "r") as file:
    data = json.load(file)

records = data.get("prices")

cities_code = []

# ____________ GETTING IATA for CITY via TEQUILLA FLIGHT API____________________
for record in records:
    city = record.get("city")

    HOST_DOMAIN = "https://api.tequila.kiwi.com"
    location_api = f"{HOST_DOMAIN}/locations/query"
    header = {
        "apikey": TEQUILLA_FLIGHT_API_TOKEN,
    }
    parameters = {
        "term": city,
        "location_types": "city",
    }
    location_response = requests.get(url=location_api, params=parameters, headers=header)
    data = location_response.json()
    cities_code.append(data.get("locations")[0]['code'])

print(cities_code)

# ----------------- updating sheety ------------
row_id = 2
for city_code in cities_code:
    sheety_put_url = f'https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/flight/prices/{row_id}'
    sheety_headers = {
        "Authorization": SHEETY_TOKEN
    }
    update_body = {
        "price": {
            "iataCode": city_code,
        }
    }
    resp = requests.put(url=sheety_put_url, headers=sheety_headers, json=update_body)
    print(resp.text)

    row_id += 1



