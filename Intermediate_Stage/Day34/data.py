import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
    "difficulty": "medium"
}

# our questions are gotten from the Open Trivial Database
URL = "https://opentdb.com/api.php"
response = requests.get(url=URL, params=parameters)
question_data = response.json()['results']
