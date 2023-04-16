"""" This is a number guessing game """
import random

logo = """
  _   _                 _                  _____                     _                _____                       
 | \ | |               | |                / ____|                   (_)              / ____|                      
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___  
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/ 
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___| 
                                                                              __/ |                               
                                                                             |___/                                """
print(logo)
print("Welcome to the Number Guessing Game")

# Create a number list:
number_list = []
for _ in range(0, 1001):
    number_list.append(_)

# Set the answer:
answer = random.choice(number_list)


# FUNCTIONS DEFINITION #############
def hard():
    """ This function checks user guess on the difficulty level: HARD and plays the game"""
    print(f"I'm thinking of a number between {number_list[number_list.index(answer) - 50]}"
          f" and {number_list[number_list.index(answer) + 50]}")
    attempts = 5
    print(f"You have {attempts} attempts")
    attempts_exhausted = False
    while (not attempts_exhausted) and (attempts > 0):
        guess = int(input("\nMake a guess:  "))
        if guess == answer:
            print(f"\nYou got it! The answer was {answer}")
            attempts_exhausted = True
        elif guess > answer:
            print("\nToo high\nGuess Again")
            print(f"You have {attempts - 1} attempts remaining to guess the number.")
            attempts -= 1
        else:
            print("\nToo low\nGuess Again")
            print(f"You have {attempts - 1} attempts remaining to guess the number.")
            attempts -= 1

    # print the answer when the user attempt is exhausted:
    if attempts == 0:
        print(f"\nThe answer is: {answer}")


def easy():
    """ This function checks user guess on the difficulty level: EASY and plays the game"""
    print(f"I'm thinking of a number between {number_list[number_list.index(answer) - 10]}"
          f" and {number_list[number_list.index(answer) + 10]}")
    attempts = 10
    print(f"You have {attempts} attempts")
    attempts_exhausted = False
    while (not attempts_exhausted) and (attempts > 0):
        guess = int(input("\nMake a guess:  "))
        if guess == answer:
            print(f"\nYou got it! The answer was {answer}")
            attempts_exhausted = True
        elif guess > answer:
            print("\nToo high\nGuess Again")
            print(f"You have {attempts - 1} attempts remaining to guess the number.")
            attempts -= 1
        else:
            print("\nToo low\nGuess Again")
            print(f"You have {attempts - 1} attempts remaining to guess the number.")
            attempts -= 1

    # print the answer when the user attempt is exhausted:
    if attempts == 0:
        print(f"\nThe answer is: {answer}")


# FUNCTIONS DEFINITION END ##############


# Get the difficulty level from the user:
difficulty = input("Choose your difficulty. Type 'easy' or 'hard':  ").lower()

# Check players difficulty level AND plays call the corresponding function:
if difficulty == 'hard':
    hard()
elif difficulty == 'easy':
    easy()
else:
    print("Invalid Option. Try Again")
