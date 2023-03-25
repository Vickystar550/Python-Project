# This program marks a spot in the matrix of blank space

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map_list = [row1, row2, row3]

# Print the map for the players to see:
print(f"{row1}\n{row2}\n{row3}")

print("Enter a 2-digit number, the 1st entry specify column, second specify row")
position = input("Where do you want to put the treasure?\n")

# Extracting row and col from the user input
row = int(position[1]);
col = int(position[0])

# Row One as in the map
if row == 1:
    if col == 1:
        row1[0] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif col == 2:
        row1[1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif col == 3:
        row1[2] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid Position!")
# Row Two as in map
elif row == 2:
    if col == 1:
        row2[0] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif col == 2:
        row2[1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif col == 3:
        row2[2] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid Position!")
# Row Three as in map
elif row == 3:
    if col == 1:
        row3[0] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif col == 2:
        row3[1] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    elif col == 3:
        row3[2] = "X"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid Position!")
else:
    print("Invalid Position!")
