""""Calculate the average student height from the list of height"""

print("Welcome to average height calculator")
heights = input("Enter the heights separated by space\n").split()

# print(heights)

# Looping through heights; Avoid the use of len() and sum() functions!!!
height_sum = 0
height_count = 0
for height in heights:
    height_sum += float(height)
    height_count += 1

average_height = height_sum / height_count

print(f"The average height is: {round(average_height)}")
