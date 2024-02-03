"""This game displays the highest bidder from a dict of bidders."""

print("Welcome to the Blind Bidding Game")

# Creating an empty dict to house bidders and their bids:
bidders_dict = {}


def user_input():
    """ This function prompt bidders for inputs and check if other bidders exist"""
    name = input("What is your name?\n")
    bid = input("What's your bid?\n")
    bidders_dict[name] = bid


def highest_bid():
    """This function checks for the highest bid and print it together with the bidder"""
    biggest_bid = 0
    biggest_bidder_name = ""
    for key in bidders_dict:
        if int(bidders_dict[key]) > biggest_bid:
            biggest_bid = int(bidders_dict[key])
            biggest_bidder_name = key.title()
    print("The Highest Bid is {} and it was made by {}".format(biggest_bid, biggest_bidder_name))


game_on = True
while game_on:
    user_input()
    # check if there are other bidders:
    other_bidders = input("Are there any other bidders? Type 'Yes' or 'No'\n").lower()
    if other_bidders != "yes" or other_bidders != "y":
        game_on = False

highest_bid()


