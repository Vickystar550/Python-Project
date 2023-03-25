# This program collect names of group of friends at the restaurant and randomly select who pays the bills.

import random

name = input("Enter everybody\'s name separated by comma\n")

name_list = name.split(", ")
print(name_list)

per_son = random.choice(name_list)
print(per_son)

print(f"The total bill will be pay by {per_son}")