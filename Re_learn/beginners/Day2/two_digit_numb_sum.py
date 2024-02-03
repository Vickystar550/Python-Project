""" This code add digits in a two-digit number"""

# Get the two-digits number:
two_digit_number = input("Enter any two-digits number:\n")

# Extract the individual digits:
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])

# Add the two digits:
digit_sum = first_number + second_number

# Print the results:
print(f"The sum of the two-digits number is: {digit_sum}")