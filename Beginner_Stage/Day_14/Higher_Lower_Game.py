""" This is a Higher and Lower Game"""

import random
import art
import game_data

SCORE = 0  # A global constant
print(art.logo)

# Start game, setting SCORE to Zero
while SCORE > -1:
    # Create a variable for both option A and B:
    account_a = game_data.data[random.randint(0, 49)]
    account_b = random.choice(game_data.data)

    # Check if the two account are the same:
    if account_a == account_b:
        account_a = random.choice(game_data.data)

    print(f"\nCompare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(art.vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

    # Ask for user option
    user_choice = input("Who has more followers? Type 'A' or 'B':   ").lower()

    # Checks user input
    if user_choice == 'a':
        # compare
        if account_a['follower_count'] > account_b['follower_count']:
            print(f"You're right! Correct score: {SCORE + 1}")
            SCORE += 1
        else:
            print(f"You're wrong! Final score: {SCORE}")
            SCORE = -1
    elif user_choice == 'b':
        # compare
        if account_a['follower_count'] < account_b['follower_count']:
            print(f"You're right! Correct score: {SCORE + 1}")
            SCORE += 1
        else:
            print(f"You're wrong! Correct score: {SCORE}")
            SCORE = -1
    else:
        print("Invalid Option")
        SCORE = -1
