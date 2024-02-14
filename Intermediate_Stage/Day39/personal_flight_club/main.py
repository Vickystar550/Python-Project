import requests
import json
from datetime import datetime
import smtplib

SHEETY_TOKEN = "Enter your api key here"
TEQUILLA_FLIGHT_API_TOKEN = "Your api key here"

def getting_rows():
    # Getting rows from sheety: My Flight Deals
    sheety_url = "https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/flight/prices"

    sheety_headers = {
        "Authorization": SHEETY_TOKEN
    }
    sheety_response = requests.get(url=sheety_url, headers=sheety_headers)
    records_list = sheety_response.json()

    with open("sheety_data.json", "w") as file:
        json.dump(records_list, file, indent=4)


def reading_from_row_file():
    with open("sheety_data.json", "r") as file:
        data = json.load(file)
    return data.get("prices")


cities_code = []


def get_iata_for_each_city():
    # ____________ GETTING IATA for CITY via TEQUILLA FLIGHT API____________________
    records = reading_from_row_file()

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


def updating_sheety_with_city_iatacode():
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


def play_program():
    # 1. get rows
    getting_rows()
    # 2. get iata for each city
    get_iata_for_each_city()
    # update rows in sheety
    updating_sheety_with_city_iatacode()
    # check for the cheapest flight and send emails:
    searching_for_cheapest_flight()


play_program()


def searching_for_cheapest_flight():
    records = reading_from_row_file()

    for record in records:
        city = record.get("city")
        lowest_price = record.get("lowestPrice")

        HOST_DOMAIN = "https://api.tequila.kiwi.com/v2"
        search_endpoint = f"{HOST_DOMAIN}/search"
        header = {
            "apikey": TEQUILLA_FLIGHT_API_TOKEN,
        }
        parameters = {
            "fly_from": "LOS",
            "flt_to": city,
            "date_from": datetime.now().strftime("%d/%m/%Y"),
            "date_to": datetime(year=2024, month=2, day=29).strftime("%d/%m/%Y"),
            "return_from": datetime(year=2024, month=8, day=1).strftime("%d/%m/%Y"),
            "return_to": datetime(year=2024, month=8, day=31).strftime("%d/%m/%Y"),
            "curr": "USD",
        }

        r = requests.get(url=search_endpoint, headers=header, params=parameters)
        print(r.text)
        data = r.json()

        cheapest_route = data.get('data')[0]
        route_price = cheapest_route.get("price")

        if route_price < lowest_price:
            # send email
            pass




