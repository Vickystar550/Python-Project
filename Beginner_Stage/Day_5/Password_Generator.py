""" This is a password generator program. It generates password from user's input"""
import random

print("Welcome to Password Generator")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

# Stored letters, numbers and symbols:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Create a list to hold the password
password_list = []

# Adding letters to password_list
for i in range(nr_letters):
    password_list.append(random.choice(letters))
# Adding symbols to password_list
for i in range(nr_symbols):
    password_list.append(random.choice(symbols))
# Adding numbers to password_list
for i in range(nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)

Easy_Password = ""
Hard_Password = ""

# EASY LEVEL --- ORDER NOT RANDOMISED
for i in range(len(password_list)):
    Easy_Password += password_list[i]
print(f"Your EASY Password is: {Easy_Password}")

# HARD LEVEL --- ORDER RANDOMISED
for i in range(len(password_list)):
    Hard_Password += str(random.choice(password_list))
print(f"Your HARD Password is: {Hard_Password}")

# Your can use the random.shuffle() method to shuffle the list content when printing the hard password
