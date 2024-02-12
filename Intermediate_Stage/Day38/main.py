import requests
import json
import datetime as dt
import os

API_ID = "enter your api_id"
API_KEY = "enter your key"
SHEETY_AUTH = "enter your sheety api_key"


# Natural Language for Exercise API ------------------------

HOST_DOMAIN = "https://trackapi.nutritionix.com"
natural_language_exercise_endpoint = f"{HOST_DOMAIN}/v2/natural/exercise"

headers = {
    "x-app-id": str(os.environ.get("NLP_API_ID")),
    "x-app-key": str(os.environ.get("NLP_API_KEY")),
    'Content-Type': 'application/json'
}
body_parameters = {
    "query": "python programming for 5 hours"
}

exercise_response = requests.post(url=natural_language_exercise_endpoint, headers=headers, json=body_parameters)
print(exercise_response.status_code)
print(exercise_response.text)
exercise_data = exercise_response.json()

# saving to a json file
with open("exercise_data.json", "w") as file:
    json.dump(exercise_data, fp=file, indent=4)

# getting the required data:
exercise_name = exercise_data.get("exercises")[0]["user_input"]
duration = exercise_data.get("exercises")[0]["duration_min"]
calories = exercise_data.get("exercises")[0]["nf_calories"]

# ------------ SHEETY ------------------

sheety_endpoint = "https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/100CodingTracking/workouts"

sheety_header = {
    "Authorization": SHEETY_AUTH,
    'Content-Type': 'application/json'
}

post_body = {
    "workout": {
        "date": f'{dt.datetime.now().strftime("%d/%m/%Y")}',
        "time": f'{dt.datetime.now().strftime("%H:%M:%S")}',
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=post_body, headers=sheety_header)
print(sheety_response.text)
print(sheety_response.json())
