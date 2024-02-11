import requests

domain_url = "https://pixe.la"
new_user_endpoint = f"{domain_url}/v1/users"
TOKEN = "your token here"
USERNAME = "your username here"
GRAPH_ID = "graph1"

pixel_creation_endpoint = f"{domain_url}/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

header_parameters = {
    "X-USER-TOKEN": TOKEN
}

pixel_data = {
    "date": "20240211",
    "quantity": "3.5"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header_parameters)
print(response.text)
