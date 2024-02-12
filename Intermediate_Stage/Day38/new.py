import requests
import json

API_ID = "enter your api_id"
API_KEY = "enter your api_key"

# Natural Language Nutrients API ------------------------

HOST_DOMAIN = "https://trackapi.nutritionix.com"
natural_language_nutrients_endpoint = f"{HOST_DOMAIN}/v2/natural/nutrients"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json'
}
body_parameters = {
    "query": "I ate 3 eggs, yogurt with toasted bread"
}

nutrient_response = requests.post(url=natural_language_nutrients_endpoint, headers=headers, json=body_parameters)
nutrient_response.raise_for_status()
nutrient_data = nutrient_response.json()


with open("nutrient_data.json", "w") as file:
    json.dump(nutrient_data, fp=file, indent=4)

