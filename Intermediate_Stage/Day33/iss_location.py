import requests

# Get the iss position from the ISS API endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# extracting the jsonic data from the response object: this is a <dict> type
data = response.json()

# get the iss_position value
iss_position = data["iss_position"]

# get the latitude and longitude
latitude = iss_position.get("latitude")
longitude = iss_position.get("longitude")

# save the latitude and longitude to a tuple
position = (latitude, longitude)

print(position)

