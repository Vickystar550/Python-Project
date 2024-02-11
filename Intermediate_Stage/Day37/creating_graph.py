import requests

domain_url = "https://pixe.la"
new_user_endpoint = f"{domain_url}/v1/users"
TOKEN = "your token here"
USERNAME = "your username here"

# creating a new graph:
graph_endpoint = f"{new_user_endpoint}/{USERNAME}/graphs"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "100 Days of Code",
    "unit": "time",
    "type": "float",
    "color": "sora"
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
print(graph_response.text)
