"""" This is a Hangman game """

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter in Hangman\'s word:\n").lower()

# for i in chosen_word:
