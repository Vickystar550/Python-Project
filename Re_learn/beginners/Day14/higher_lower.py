# importing libraries and files
import random
import art
import data


def ask_and_check_user_input():
    """This function ask for user option, checks it and return number of followers from the account of their choice"""
    user_option = input("\nWho has more followers? Type 'A' or 'B':\t").lower()
    if user_option == 'a':
        return first_account['follower_count']
    elif user_option == 'b':
        return second_account['follower_count']


def more_followers(data_x, data_y):
    """This function takes in the two accounts and returns the one with highest number of followers"""
    max_count = max([data_x['follower_count'], data_y['follower_count']])
    max_index = [data_x['follower_count'], data_y['follower_count']].index(max_count)
    if max_index == 0:
        return data_x
    else:
        return data_y


# Create the first account
first_account = random.choice(data.data)
# Print the first logo
print(f"{art.logo}")

# Initialize the score variable:
score = 0
while True:
    # Create the second account:
    second_account = random.choice(data.data)
    # keep checking until the second_account is not the same as the first
    while second_account == first_account:
        second_account = random.choice(data.data)

    print(f"\nCompare A: {first_account['name']}, {first_account['description']}, from {first_account['country']}")
    print(f"\n{art.vs}")
    print(f"Against B: {second_account['name']}, {second_account['description']}, from {second_account['country']}")

    # Get the user answer:
    user_answer = ask_and_check_user_input()
    # FROM the account with the highest followers, GET the correct answer:
    correct_answer = more_followers(first_account, second_account)['follower_count']

    # reassign the first_account with the second one:
    first_account = second_account

    # Check the user answer against the correct answer:
    if user_answer != correct_answer:
        print(f"Sorry! That is not correct. Your final score is {score}")
        break
    else:
        score += 1
        print(f"\nCongratulations! Your score is {score}")
