"""This program checks the compatibility between two people"""

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# Combining both names and make it the same case
name1_name2 = (name1 + name2).upper()

# Counting for TRUE:
T = name1_name2.count("T"); R = name1_name2.count("R"); U = name1_name2.count("U"); E = name1_name2.count("E")

# Counting for LOVE:
L = name1_name2.count("L"); O = name1_name2.count("O"); V = name1_name2.count("V")

# Summing for True:
sum_true = T + R + U + E

# Summing for Love:
sum_love = L + O + V + E

# Concatenating the value of TRUE and LOVE:
true_love = int(str(sum_true) + str(sum_love))



if (true_love < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")

