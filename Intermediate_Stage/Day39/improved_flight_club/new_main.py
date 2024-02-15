from sheety_account import SheetyFlightManger
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheety_data = SheetyFlightManger()
flight_search = FlightSearch()
notify = NotificationManager()

# 1. get rows of the Google sheets: prices and users
sheety_data.get_rows("prices")
f_data = sheety_data.destination_data
# print(f_data)

sheety_data.get_rows("users")
user_database = sheety_data.users_data
# print(user_database)


# 2. get iata for each city
for record in f_data:
    if record.get("iataCode") == "":
        # get the code
        code = flight_search.get_destination_code(city_name=record.get("city"))
        record["lowestPrice"] = code

        # update row with code
        row_id = record.get("id")
        sheety_data.update_iatacode(row_id=row_id, city_code=code)


# 3. search for the cheapest flight and send emails:
search_result = flight_search.search_for_cheapest_flight(f_data)
print(search_result)
print(type(search_result))


# 4. send notification:
for i in range(len(f_data)):
    a1 = search_result[i]
    a2 = f_data[i]
    a3 = user_database[i]

    if a2['price'] > a1['price']:
        email = a3["email"]
        message = (f"Low price alert! Only £{a1.price} to fly from"
                   f" {a1.origin_city}-{a1.origin_airport} to "
                   f"{a1.destination_city}-{a1.destination_airport}, "
                   f"from {a1.out_date} to {a1.return_date}.")

        notify.send_mail(user_email=email, message=message)
