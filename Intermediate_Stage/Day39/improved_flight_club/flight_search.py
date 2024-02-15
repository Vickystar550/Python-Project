import requests
from pprint import pprint

TEQUILLA_FLIGHT_API_TOKEN = "enter here"

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
        location_response = requests.get(url=location_api, params=parameters, headers=header)
        data = location_response.json()
        return data.get("locations")[0]['code']
    