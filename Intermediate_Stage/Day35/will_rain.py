import requests
from twilio.rest import Client

#
# API_KEY = os.environ.get("OWN_API_KEY")
# account_sid = os.environ.get("TWILLO_ACCOUNT_SID")
# auth_token = os.environ.get("TWILLO_ACCOUNT_TOKEN")


parameters = {
    "lat": 4.847800,
    "lon": 7.850800,
    "appid": "enter your api key",
    "cnt": 4
}

url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)


will_shine = False
for item in data.get("list"):
    weather_id = item["weather"][0]["id"]
    if weather_id > 700:
        will_shine = True


if will_shine:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+19252414618',
        to='+2348105662218'
    )
    print(message.status)
