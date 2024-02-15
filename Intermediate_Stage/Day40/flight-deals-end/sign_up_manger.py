import requests

SHEETY_TOKEN = "Enter your key"


class SignUp:
    def __init__(self):
        self.url = "https://api.sheety.co/3dfc9c99ec54d671b966b4ebc4856cf6/flight/users"
        self.database = []
        self.header = {
            "Authorization": SHEETY_TOKEN
        }

    def get_rows(self):
        """Get rows from the specified sheet in the sheety project files"""
        response = requests.get(url=self.url, headers=self.header)
        records_list = response.json()
        data = records_list.get("users")

        self.database = data
        return data

    def sign_up(self):
        """Create a user database by querying user via sign-up"""
        print("welcome to the Victor Nice's Flight Club")
        print("We find the best flight deals and email you")

        first_name = input("\nWhat is your first name?\n").title()
        last_name = input("\nWhat is your last name?\n").title()
        email = input("\nWhat is your email?\n").lower()
        email_again = input("\nType your email again.\n").lower()

        if email == email_again:
            # check is user already exits
            if self.already_exist(email_=email):
                print("Already our subscriber")
            else:
                print("You're in the club")
                body = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "email": email
                    }
                }
                r = requests.post(url=self.url, headers=self.header, json=body)
                print(r.text)
                # return true when a new user is successfully created
                return True
        else:
            print("EmailMatchError. Please enter your email correctly")

    def already_exist(self, email_) -> bool:
        """check if user already exists"""
        if email_ is None:
            email = input("\nWhat is your email?\n").lower()
        else:
            email = email_

        database = self.get_rows()
        for user in database:
            if email == user.get("email"):
                return True


signing_ = SignUp()
signing_.sign_up()
