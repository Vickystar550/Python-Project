from datetime import datetime, timedelta
import html

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


# creating objects:
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# getting rows from sheety spreadsheet
price_sheet_data = data_manager.get_rows("prices")
user_database = data_manager.get_rows("users")

# set starting destination
ORIGIN_CITY_IATA = "LON"

# updating rows in price spreadsheet with iata code
for destination in price_sheet_data:
    if destination['iataCode'] == "":
        destination['iataCode'] = flight_search.get_destination_code(destination["city"])
        data_manager.update_iatacode(city_code=destination['iataCode'], row_id=destination['id'])

# set tomorrow's time and six month .........
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# loop through each subscriber account: that is each record in the users spreadsheet
for i in range(0, len(user_database)):
    # for each user account
    user = user_database[i]

    # loop through the flight prices spreadsheet
    for k in range(0, len(price_sheet_data)):
        # for each travel destination,
        destination = price_sheet_data[k]

        # search for a flight from the Origin City to the Destination City from the
        # from_time to the to_time variable defined above, it returns a flight object
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        # if the returned flight object is None, move to the next iteration
        if flight is None:
            continue

        # else do this operation: check if the flight price is < the destination assumed lowestPrice
        if flight.price < destination["lowestPrice"]:
            # prepare a message to mail to our subscriber
            message = html.unescape(f"Low price alert! Only £{flight.price} to fly from "
                                    f"{flight.origin_city}-{flight.origin_airport} "
                                    f"to {flight.destination_city}-{flight.destination_airport}, "
                                    f"from {flight.out_date} to {flight.return_date}.")
            ######################
            if flight.stop_overs > 0:
                # print this if we've any stop-overs
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)
            #######################

            # print(user.get("email"))
            notification_manager.send_mail(user_email=user['email'],
                                           message=message
                                           )
