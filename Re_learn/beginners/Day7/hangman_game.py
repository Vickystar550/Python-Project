"""This is your amazing Hangman Game"""

#-----------------------Importing the necessary files and library---------------
from hangman import words
from hangman_art import *
import random

#------------------------------Initializing Variables---------------------------
# Select a random word for the game
hang_word = random.choice(words.split()).lower()
# Initialize a variable filling it with blank spaces:
blanks = ["_" for i in hang_word]
# Set the game trial to 7. This is the maximum trial if the player guess is incorrect
trial = 7

# -------------------------------STARTING THE GAME------------------
print(logo)
print("\nWelcome to this Brainstorming Hangman Game")
print(f"\nGuess a {len(hang_word)}-lettered word from the Hangman Dictionary")

while trial > 0 and "_" in blanks:
    # Prompting player for a guess letter:
    usr_input = input("\nPlease guess a letter:").lower()

    # Checking the player's entry against every letter in hang_word:
    if usr_input in hang_word:

        # hold hang_word in another variable:
        h_word = hang_word

        # Set a while loop to check for repeated cases of player's input:
        while usr_input in h_word:
            
            # Catch the inputed letter index in h_word:
            l_index = h_word.index(usr_input)

            # Replace the 1st occurence of the player's input with an underscore in h_word:
            h_word = h_word.replace(usr_input, "_", 1)

            # Replace the blanks variable with player's input at the same index as
            #  it matches the hang_word or h_word:
            blanks[l_index] = usr_input
        
        # Print the blanks variable as a joined string:
        print("".join(blanks))

    else:
        # Reduce the trial count and print a message:
        trial -= 1
        print(f"\nWRONG CHOICE! You have {trial} trail left")

        # Print each stage of the hangman art corresponding to the amount of trial left:
        print(stages[trial])
        
if "".join(blanks) == hang_word:
    print(f"\nCongratulation, your guess was correct and complete. The hangword was {hang_word.upper()}\n")
else:
    print("\nYou didn't pass the challenge!\n")
    print(f"The word was {hang_word.upper()}\n")
    