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
right_guess = random.randint(1, 100)
is_user_right = False

print(logo)
print("Welcome to the amazing number guessing game!\n"
      "I'm thinking of a number between 1 and 100\n")
difficulty = input("\nChoose a difficulty: Type 'easy' or 'hard'\t").lower()


if difficulty in ['easy', 'e']:
    attempt = 10
    for _ in range(10):
        print(f"\nYou have {attempt} remaining to guess the number.")
        guess = int(input("Make a guess:\t"))
        if guess == right_guess:
            print("\nCongratulations, you got it right!\n")
            is_user_right = True
            break
        elif guess < right_guess:
            print("\nToo low\nGuess again\n")
        elif guess > right_guess:
            print("\nToo high\nGuess again\n")
        else:
            print("Invalid Guess")
        attempt -= 1
elif difficulty in ['hard', 'h']:
    attempt = 5
    for _ in range(5):
        print(f"\nYou have {attempt} remaining to guess the number.")
        guess = int(input("Make a guess:\t"))
        if guess == right_guess:
            print("\nCongratulations")
            is_user_right = True
            break
        elif guess < right_guess:
            print("\nToo low\nGuess again\n")
        elif guess > right_guess:
            print("\nToo high\nGuess again\n")
        else:
            print("\nInvalid Guess")
        attempt -= 1

if difficulty not in ['easy', 'e', 'hard', 'h']:
    print("\nInvalid difficulty choice!")
elif not is_user_right:
    print(f"The correct number is {right_guess}. You fail!!")
