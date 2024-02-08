import smtplib
import datetime as dt
import pandas
import random

# ------ CONSTANTS VARIABLES -----------
LETTER_TEMPLATES = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
NAME_HOLDER = "[NAME]"

# PLEASE input your Google Mail service login details below before running this file:
MY_PASSWORD = None  # enter your password
MY_EMAIL = None  # your sending email address
# ----------------------------------------------

# Get the birthday csv data to a pandas dataframe
birthday_data = pandas.read_csv("birthdays.csv")

# Get today's date
today = dt.datetime.today()

# Get a dataframe with people whose birth-month is this month
this_month = birthday_data[birthday_data.month == today.month]

# Get a dataframe with people whose birthday is today
this_day = this_month[this_month.day == today.day]

# Create a list of celebrants from this_day dataframe. Each celebrant is a dictionary
celebrants = this_day.to_dict(orient="records")

# Check if there is any celebrant
if len(celebrants) > 0:
    # Loop over the celebrants list
    for celebrant in celebrants:
        # get the celebrant name and email:
        name = celebrant.get("name")
        email = celebrant.get("email")

        # get a random letter template for each celebrant
        letter = random.choice(LETTER_TEMPLATES)

        # open the letter and make changes to it: make it a personalized letter for each celebrant
        with open(letter, mode="r") as letter_file:
            # read the letter's content
            content = letter_file.read()
            # replace the content with the sender's identity as your own
            content = content.replace("Angela", "Victor Nice")
            # replace the content with the name holder after the Dear salutation with the celebrant name
            birthday_letter = content.replace(NAME_HOLDER, name)

        # open a smtp connection:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # make it secure with TLS
            connection.starttls()
            # login with your details as the sender
            connection.login(MY_EMAIL, MY_PASSWORD)     # remember to enter your login details: in string format
            # send the letter
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday\n\n{birthday_letter}")
else:
    print("Oops! No birthday celebrant for today")
