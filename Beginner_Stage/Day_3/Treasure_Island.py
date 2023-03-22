"""This is a treasure island challenge"""

print("""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|""")

print("Welcome to Treasure Island. Your mission to find the treasure")

way = input("You\'re at the crossroad. Which way do you want to go? R (or Right) L (for Left)\n").lower()


if way == "l":
    swim_wait = input("Would you love to swim or wait? W (for wait) S (swim)\n").lower()
    if swim_wait == "w":
        door = input("Which door do you want choose? R (red) B (blue) Y (yellow)\n").lower()
        if door == "y":
            print("You Win!")
        elif door == "b":
            print("Eaten by beasts. Game Over!!!")
        elif door == "r":
            print("Burned by Fire. Game Over!!!")
        else:
            print("Game Over!!!")
    else:
        print("Attacked by trout. Game Over!!!")
else:
    print("You have fallen into a hole. Game Over!!!")