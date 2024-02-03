"""A Treasure Island calculator"""


icon = """_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|\n"""

print(icon) 

print("Welcome to the Treasure Island\nYour mission is to find the Treasure\n")

direction = input("Which direction do you want to go? L(left) or R(right)\n").lower()

if direction == "l":
    choice = input("Do you wishh to swim S or to wait W\n").lower()

    if choice == "s":
        print("Interesting to know you're hydrophilic, but this got you drowning in a deadly sea. GAME OVER!!!")
    elif choice == "w":
        door = input("Which colored door do you think the treasure is store?  R(red), B(blue) or Y(yellow)\n").lower()

        if door == "b":
            print("Congratulations, you win!!")
        else:
            print("Sorry, GAME OVER")
    else:
        print("You made an invalid choice!!! GAME OVER")
else:
    print("You have entered the wrong direction. GAME OVER!!!")
