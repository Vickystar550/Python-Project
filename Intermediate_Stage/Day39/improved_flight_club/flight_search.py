import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILLA_FLIGHT_API_TOKEN = "enter your passwd"


class FlightSearch:
    def __init__(self):

        self.host_domain = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": TEQUILLA_FLIGHT_API_TOKEN,
        }

    def get_destination_code(self, city_name):
        """Get the IATA code for any city"""
        location_api = f"{self.host_domain}/locations/query"
        parameters = {
            "term": city_name,
            "location_types": "city",
        }
        location_response = requests.get(url=location_api, params=parameters, headers=self.headers)
        data = location_response.json()
        return data.get("locations")[0]['code']

    def search_for_cheapest_flight(self, records):
        result = []

        for record in records:
            city = record.get("city")

            search_endpoint = f"{self.host_domain}/v2/search"
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

            r = requests.get(url=search_endpoint, headers=self.headers, params=parameters)
            print(r.text)

            try:
                data = r.json().get('data')[0]
            except IndexError:
                print("No flight available for destination")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
                result.append(flight_data)
        return result
