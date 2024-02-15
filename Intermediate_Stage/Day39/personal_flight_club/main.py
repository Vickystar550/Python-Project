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


def get_iata_for_each_city(records):
    # ____________ GETTING IATA for CITY via TEQUILLA FLIGHT API____________________
    cities_code = []

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
    return cities_code


def updating_sheety_with_city_iatacode(cities_code):
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
    # 1. get rows which is saved in a json file
    getting_rows()
    # 2. read records from stored json file
    row_records = reading_from_row_file()
    # 3. get iata for each city
    c_codes = get_iata_for_each_city(records=row_records)
    # 4. update rows in sheety
    updating_sheety_with_city_iatacode(cities_code=c_codes)
    # 5. check for the cheapest flight and send emails:
    search_result = searching_for_cheapest_flight(records=row_records)
    send_notification(search_result=search_result, records=row_records)


play_program()


def searching_for_cheapest_flight(records):
    result = []

    for record in records:
        city = record.get("city")
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
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        r = requests.get(url=search_endpoint, headers=header, params=parameters)
        print(r.text)

        try:
            data = r.json().get('data')[0]
        except IndexError:
            print("No flight available for destination")
            return None
        else:
            result.append({
                "price": data["price"],
                "origin_city": data["route"][0]["cityFrom"],
                "origin_airport": data["route"][0]["flyFrom"],
                "destination_city": data["route"][0]["cityTo"],
                "destination_airport": data["route"][0]["flyTo"],
                "out_date": data["route"][0]["local_departure"].split("T")[0],
                "return_date": data["route"][1]["local_departure"].split("T")[0]
            })
        return result


def send_notification(search_result, records):
    for i in range(records):
        a1 = search_result[i]
        a2 = records[i]
        if a1["price"] < a2["lowestPrice"]:
            # send mail notification

            message = (f"Low price alert! Only £{a1.price} to fly from"
                       f" {a1.origin_city}-{a1.origin_airport} to "
                       f"{a1.destination_city}-{a1.destination_airport}, "
                       f"from {a1.out_date} to {a1.return_date}.")

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject: Your Flight is Ready\n\n{message}")


