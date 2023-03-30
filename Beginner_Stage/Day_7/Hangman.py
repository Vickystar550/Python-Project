"""" This is a Hangman game """

import random
from hangman_words import words
import hangman_art

# VARIABLE SETTING: ####
# 1. Choose a random word from list of words:
chosen_word = random.choice(words.split())

# 2. Create a blank variable with an underscore that will be filled with user's input:
blank_list = []
for i in range(len(chosen_word)):
    blank_list += "_"

# START THE GAME: ####
print(hangman_art.logo)
print(f"Guess a {len(chosen_word)}-lettered word in the Hangman's Dictionary")
lives = 7
end_of_game = False
while not end_of_game:
    # Ask for user input
    guess_letter = input("Enter a letter:\n").lower()

    # Loop and check if guess_letter is in the chosen word, replace blank_list with guess_letter:
    for i in range(len(chosen_word)):
        if guess_letter == chosen_word[i]:
            blank_list[i] = guess_letter

    # When the guess letter isn't in the chosen word:
    if guess_letter not in chosen_word:
        print(f"You have entered \'{guess_letter}\' which is not a letter in the chosen word. You lose a life")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You have lost!!!😭😭😭")

    # check if user has filled all the blank spaces in blank_list:
    if "_" not in blank_list:
        end_of_game = True
        print("You win!!!🥰🥰🥰")
