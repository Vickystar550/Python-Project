import requests
import datetime as dt

"""This api get the sunrise and sunset time based on your location"""

URL = "https://api.sunrise-sunset.org/json"
TZID = "Africa/Lagos"
LATITUDE = "6.6009"
LONGITUDE = "3.4882"

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "tzid": TZID,
    "formatted": 0
}

# send the request
response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()

result = data.get('results')

# getting the sunrise and sunset as hour string
sunrise = result.get('sunrise').split("T")[-1].split(":")[0]
sunset = result.get('sunset').split("T")[-1].split(":")[0]

time_now = dt.datetime.now()

print(sunset)

print(sunrise)

print(time_now.hour)