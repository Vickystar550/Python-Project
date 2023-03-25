"""This program print out Head os Tail based on randomization"""

import random

random_number = random.randint(0, 1)

if random_number == 0:
    print("Heads")
else:
    print("Tails")