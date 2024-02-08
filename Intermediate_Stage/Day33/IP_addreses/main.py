import requests
import json


def get_public_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        print(data.get("ip"))
        return data
    except requests.RequestException:
        return None


def ip_details(resp):
    try:
        # read stored json data in a json file, and update it with the new_data
        with open("location_info.json", "r") as ip_file:
            # reading old data
            data = json.load(ip_file)
    except FileNotFoundError:
        # create a new json file and store the new_data:
        with open("location_info.json", "w") as ip_file:
            json.dump(resp, ip_file, indent=4)
    else:
        # updating old data with new response
        data.update(resp)
        # save next entry to the created json file:
        with open("location_info.json", mode="w") as new_file:
            json.dump(data, new_file, indent=4)


def simple_write(resp):
    """append to an already existing file"""
    with open("location_info.json", "a") as file:
        json.dump(resp, file, indent=4)


x = get_public_ip()
simple_write(resp=x)
