""" This is a password generator program"""
from random import choice, randint, shuffle


# Stored letters, numbers and symbols:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password():
    """Create and return a password"""

    p_letters = [choice(letters) for i in range(randint(0, 8))]
    p_symbols = [choice(symbols) for i in range(randint(2, 4))]
    p_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = p_letters + p_symbols + p_numbers

    shuffle(password_list)

    return "".join(password_list)
