"""This is a treasure map program that marks a spot on the map with X"""

print("Welcome to this amazing Treasure Map Game")

# create three lists to store the different 3x3 matrix entries
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]

print("""Your map is a 3 by 3 matrix pattern. This means your coordinate entry is restricted to be from 1 to 3. The spot is to be filled with X""")

# prompt for the postion or coordinate to place the X mark:
position = input("\nEnter a positive coordinate to postion your X?\n")

# adjuct the user entries to match the list indexing... i.e positon...
i_cor = int(position[0]) - 1 
j_cor = int(position[1]) - 1

# Assign the X to the map:
map[i_cor][j_cor] = "X"

# print out the result:
print(f"\n{map[0]}\n\n{map[1]}\n\n{map[2]}\n")