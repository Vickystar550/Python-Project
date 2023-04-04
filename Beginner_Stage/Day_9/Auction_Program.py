"""This program is a silent auction program."""

# Import the os module to handle clearing of the screen
import os

# Create an empty dictionary to contain user's input
auction_dict = {}

# Start the auction game
print("Welcome to the auction game")
game_on = True
while game_on:
    user_name = input("What is your name?\n")
    auction_price = float(input("What is your bid?\n"))
    auction_dict[user_name] = auction_price
    any_other = input("is there any other bidder? y or n\n")

    # clearing the screen for other user:
    os.system('clear')  # os.system('cls') for windows

    if any_other != "y":
        game_on = False

# Create a list of auction price and each auctioneer/bidder from the auction_dict:
auction_price_list = []
auctioneers = []
for key, value in auction_dict.items():
    auction_price_list.append(value)
    auctioneers.append(key)
    # print(f"The bidder is {key}, and his bid is {value}")

# check for the highest bid:
highest_bid = auction_price_list[0]
for i in auction_price_list:
    if i > highest_bid:
        highest_bid = i

# Print the auction winner
print(f"The highest bidder is {auctioneers[auction_price_list.index(highest_bid)]} with ${highest_bid} ")
