"""This is a Rock Paper Scissor Game"""
import random

print("Welcome to Rock Paper Scissor Game")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

scissor = """
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

print("hello world")
print(rock)
print(paper)

user_choice = int(input("What do you choose. Type 0 for Rock, 1 for Paper, and 2 for Scissor\n"))

computer_choice = random.randint(0, 2)
print(f"Computer Choice: {computer_choice}")

# Checking for winning:
# If user choose 0 -- Rock:
if user_choice == 0:
    if computer_choice == 1:
        print("You choose Rock, computer choose Paper. Paper wraps Rock. You Lose!!! 😰😰😰")
    elif computer_choice == 2:
        print("You choose Rock, computer choose Scissor. Rock smash Scissor. You Win!!! 😍😍😍")
    else:
        print("You choose Rock, computer choose Rock. It is\'s a tie!!! 😳😳😳")
# If user choose 1 -- Paper:
elif user_choice == 1:
    if computer_choice == 0:
        print("You choose Paper, computer choose Rock. Paper wraps Rock. You Win!!! 😍😍😍")
    elif computer_choice == 2:
        print("You choose Paper, computer choose Scissor. Scissor cut Paper. You Lose!!! 😰😰😰")
    else:
        print("You choose Paper, computer choose Paper. It is\'s a tie!!! 😳😳😳")
# If user choose 2 -- Scissor:
elif user_choice == 2:
    if computer_choice == 0:
        print("You choose Scissor, computer choose Rock. Rock smash Scissor. You Lose!!! 😰😰😰")
    elif computer_choice == 1:
        print("You choose Scissor, computer choose Paper. Scissor cut Paper. You Win!!! 😍😍😍")
    else:
        print("You choose Scissor, computer choose Scissor. It is\'s a tie!!! 😳😳😳")
# If user choose something else
else:
    print("Invalid input, you Lose!!! 🙄🙄🙄")
