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

print(rock)
print(paper)
print(scissor)

user_choice = int(input("What do you choose. Type 0 for Rock, 1 for Paper, and 2 for Scissor\n"))

computer_choice = random.randint(0, 2)

# Checking for winning:
# If user choice = 0 (Rock):
if user_choice == 0:
    print(f"Computer Choice: {computer_choice}")
    if computer_choice == 1:
        print("You chose Rock, computer chose Paper. Paper wraps Rock. You Lose!!! 😰😰😰")
    elif computer_choice == 2:
        print("You chose Rock, computer chose Scissor. Rock smash Scissor. You Win!!! 😍😍😍")
    else:
        print("You chose Rock, computer chose Rock. It is\'s a tie!!! 😳😳😳")
# If user choice = 1 (Paper):
elif user_choice == 1:
    print(f"Computer Choice: {computer_choice}")
    if computer_choice == 0:
        print("You chose Paper, computer chose Rock. Paper wraps Rock. You Win!!! 😍😍😍")
    elif computer_choice == 2:
        print("You chose Paper, computer chose Scissor. Scissor cut Paper. You Lose!!! 😰😰😰")
    else:
        print("You chose Paper, computer chose Paper. It is\'s a tie!!! 😳😳😳")
# If user chose: 2 (Scissor):
elif user_choice == 2:
    print(f"Computer Choice: {computer_choice}")
    if computer_choice == 0:
        print("You chose Scissor, computer chose Rock. Rock smash Scissor. You Lose!!! 😰😰😰")
    elif computer_choice == 1:
        print("You chose Scissor, computer chose Paper. Scissor cut Paper. You Win!!! 😍😍😍")
    else:
        print("You chose Scissor, computer chose Scissor. It is\'s a tie!!! 😳😳😳")
# If user chooses something else
else:
    print("Invalid input, you Lose!!! 🙄🙄🙄")