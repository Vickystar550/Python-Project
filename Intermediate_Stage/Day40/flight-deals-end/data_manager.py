import requests

SHEETY_TOKEN = "enter your key"


class DataManager:
    def __init__(self):
        # initialing some basic parameters
        self.url = "https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/flight"
        self.destination_data = {}
        self.users_data = {}
        self.sheety_headers = {
            "Authorization": SHEETY_TOKEN
        }

    def get_rows(self, sheet_name):
        """Get rows from the specified sheet in the sheety project files"""
        endpoint = f"{self.url}/{sheet_name}"

        response = requests.get(url=endpoint, headers=self.sheety_headers)
        records_list = response.json()
        data = records_list.get(f"{sheet_name}")

        if sheet_name == "prices":
            self.destination_data = data
        elif sheet_name == "users":
            self.users_data = data

        return data

    def update_iatacode(self, row_id, city_code):
        """update the destination IATA code to a given city code and row id of a sheet"""
        put_endpoint = f'{self.url}/prices/{row_id}'
        update_body = {
            "price": {
                "iataCode": city_code,
            }
        }
        resp = requests.put(url=put_endpoint, headers=self.sheety_headers, json=update_body)
        print(resp.text)

    def update_destination_codes(self):
        """update the IATA code to all the records in a particular sheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.url}/{city['id']}",
                json=new_data
            )
            print(response.text)

    # the signing-up part __________________

    def create_user_database(self):
        """Create a user database by querying user via sign-up"""
        print("\nWelcome to the Victor Nice's Flight Club")
        print("We find the best flight deals and email you")

        first_name = input("\nWhat is your first name?\n").title()
        last_name = input("\nWhat is your last name?\n").title()
        email = input("\nWhat is your email?\n").lower()
        email_again = input("\nType your email again.\n").lower()

        if email == email_again:
            print("You're in the club")
            url = "https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/flight/users"
            body = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email
                }
            }
            r = requests.post(url=url, headers=self.sheety_headers, json=body)
            print(r.text)
            # return true when a new user is successfully created
            return True

    def already_exist(self):
        """check if user already exists"""
        email = input("\nWhat is your email?\n").lower()
        database = self.get_rows("users")

        for user in database:
            if email == user.get("email"):
                print("Already our subscriber")
                return True
            else:
                print("Please create an account with us")
                return False

    def login_signup(self):
        decision = input("Login or Signup to Flight Club\t").lower()
        if decision in ['l', 'login']:
            self.already_exist()
        elif decision in ['s', 'signup']:
            self.create_user_database()
            return True
