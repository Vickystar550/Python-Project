import requests

# creating a new user:
domain_url = "https://pixe.la"
new_user_endpoint = f"{domain_url}/v1/users"
TOKEN = "your token here"
USERNAME = "your username here"

new_user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=new_user_endpoint, json=new_user_parameters)
# response.raise_for_status()
print(response.text)