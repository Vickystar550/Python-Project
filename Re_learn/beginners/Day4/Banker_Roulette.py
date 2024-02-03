"""This program randomly choose a name to pay for all the expenses out of given names"""

print("Welcome to the Bank Roulette Name Game!!!")

# Import the necessary library:
import random

# Get the name of the players:
names = input("\nEnter list of names you want to enroll for this game. Seperate each name by space\n\n")

# Create a list with those names:
names_list = names.split(" ")

# Generate a random number that will serve as a random index:
random_index = random.randint(0, len(names_list)-1)

# From the generated random index, select a random payer:
payer = (names_list[random_index]).upper()

# Print the random payer's name
print(f"\nThe payer for the total bill will be {payer}")