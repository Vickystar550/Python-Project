# Day 7 of 100 days

At the end of today, we will be developing a Hangman game

Hangman is a guessing for two or more players. One players thinks of a
word, phrase or sentences...

For every wrong letter you entered, you end up taking a life...

Steps followed are:
1. Set a list of words
2. make a random choice out of it
3. note the numbers of characters in word
4. ask the for user input equivalent to the number of character in word;
    create an empty variable to store the user's response.
5. loop through words to see if the character entered by user is the same
    and match with the one in word -- at the corresponding location
6. if it matches, create a variable to store the user's input
7. if it doesn't, draw a hangman at every point the user input a wrong
    character.
8. Keep asking for user input till all the blank spaces are filled
9. ...

This directory contains files used as modules in the main program(Hangman.py)
They are imported in the main file.