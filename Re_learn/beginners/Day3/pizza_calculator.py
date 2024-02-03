print("Thank you for choosing Python Pizza Deliveries\n")

size = input("What size do you want: S(small), M(medium), L(large) ?\n").lower()
add_pepperoni = input("Do you want pepperoni Y(yes) or N(no) ?\n").lower()
extra_cheess = input("Do you want extra cheese? Y(yes) or N(no) ?\n")


bill = 0

if size == "s":
    if add_pepperoni == "y":
        bill += (15 + 2)
    else:
        bill += 15
elif size == "m":
    if add_pepperoni == "y":
        bill += (15 +3)
    else:
        bill += 20
elif size == "l":
    if add_pepperoni == "y":
        bill += (25 +3)
    else:
        add_pepperoni += 25


if extra_cheess == "y":
    bill += 1

print(f"Your bill is ${bill}")