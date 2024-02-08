import requests
import json


def get_ip_address():
    """Get the ip address for the client (computer) making the request."""
    response = requests.get('https://api64.ipify.org?format=json').json()
    # print(response)
    return response["ip"]


def get_location():
    """get location info for a particular IP address
        internally call the get_ip_address function
        NOTE: using this service (ipapi endpoint) has a rate limit of 3"""
    ip_address = get_ip_address()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/')
    response.raise_for_status()
    response_data = response.json()

    # SAVING the user's location details to a json file:
    try:
        # read stored json data in a json file, and update it with the new_data
        with open("location_info.json", "r") as ip_file:
            # reading old data
            data = json.load(ip_file)
    except FileNotFoundError:
        # create a new json file and store the new_data:
        with open("location_info.json", "w") as ip_file:
            json.dump(response_data, ip_file, indent=4)
    else:
        # updating old data with new response
        data.update(response_data)

        # save next entry to the created json file:
        with open("location_info.json", mode="w") as new_file:
            json.dump(f"\n{data}", new_file, indent=4)
    finally:
        # getting short location details for immediate usage
        location_data = {
            "ip": ip_address,
            "city": response_data.get("city"),
            "region": response_data.get("region"),
            "country": response_data.get("country_name")
        }
        return location_data


get_ip_address()

