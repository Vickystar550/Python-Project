import requests
from pprint import pprint

SHEETY_TOKEN = "Enter your api key here"


class SheetyFlightManger:
    def __init__(self):
        self.url = "https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/flight"
        self.destination_data = {}
        self.users_data = {}
        self.sheety_headers = {
            "Authorization": SHEETY_TOKEN
        }

    def get_rows(self, sheet_name):
        """Get rows from the specified sheet"""

        endpoint = f"{self.url}/{sheet_name}"

        response = requests.get(url=endpoint, headers=self.sheety_headers)
        records_list = response.json()

        if sheet_name == "prices":
            self.destination_data = records_list.get(f"{sheet_name}")
        elif sheet_name == "users":
            self.users_data = records_list.get(f"{sheet_name}")

    def update_iatacode(self, row_id, city_code):
        put_endpoint = f'{self.url}/prices/{row_id}'
        update_body = {
            "price": {
                "iataCode": city_code,
            }
        }
        resp = requests.put(url=put_endpoint, headers=self.sheety_headers, json=update_body)
        print(resp.text)


