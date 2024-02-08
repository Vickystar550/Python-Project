import requests
import datetime as dt
import smtplib
import time

MY_LONGITUDE = 6.6009
MY_LATITUDE = 3.4882
MY_PASSWORD = "dfgfmhxnromfzkdd"
MY_EMAIL = "victornice550@gmail.com"


# ------------------- ISS -------------------------

def is_iss_overhead(lat, lng):
    """Return True if ISS location is overhead you based on your location"""
    latitude = lat
    longitude = lng

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_iss = response.json()

    iss_position = data_iss["iss_position"]

    iss_latitude = iss_position.get("latitude")
    iss_longitude = iss_position.get("longitude")

    if (latitude - 5 <= iss_longitude <= latitude + 5
            or longitude - 5 <= iss_latitude <= longitude):
        return True


# ------------------- SUNRISE AND SUNSET ----------------

def is_night():
    """with an api return True if its night based on your location"""
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

    resp = requests.get(url=URL, params=parameters)
    resp.raise_for_status()
    data = resp.json()
    result = data.get('results')
    # getting the sunrise and sunset as hour string
    sunrise = result.get('sunrise').split("T")[-1].split(":")[0]
    sunset = result.get('sunset').split("T")[-1].split(":")[0]

    time_now = dt.datetime.now().hour

    if time_now >= int(sunset) or time_now <= int(sunrise):
        return True


# ------------------ SENDING EMAIL -------------------
while True:
    time.sleep(60)
    if is_iss_overhead(MY_LATITUDE, MY_LONGITUDE) and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:ISS ABOVE\n\nHey lookup, ISS is currently above you")
