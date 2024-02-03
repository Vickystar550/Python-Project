"""This program generate a password extremely difficult to crack"""

# Importing the random function:
import random

# Create lists of desired numbers, alphabets and symbols to used in the password generation:
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Initialize an empty list to hold the generated password elements:
password_list = []

# Prompt the user for input:
number_count = int(input("How many numbers do you want in your password?\n"))
alphabet_count = int(input("How many alphabets do you want in your password?\n"))
symbols_count = int(input("How many symbols do you want in your password?\n"))

# Loop through number, alphabet and symbols list, adding elements to password_list
# according to the user input:
for _ in range(number_count):
    password_list.append(random.choice(numbers_list))

for _ in range(alphabet_count):
    password_list.append(random.choice(alphabet_list))

for _ in range(symbols_count):
    password_list.append(random.choice(symbols_list))


# FOR EASY CASE: (Password based on easy scenerio)
password_easy = " "
for _ in password_list:
    password_easy += _

# FOR HARD CASE: (Password based on hard scenerio)
password_hard = " "
random.shuffle(password_list)
for _ in password_list:
    password_hard += _

# Printing the passwords:
print("\nThe easier password is: {}".format(password_easy))
print(f"\nThe hardest password is: {password_hard}")