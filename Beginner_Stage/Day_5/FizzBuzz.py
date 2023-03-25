""" This is a FizzBuzz game """

# This program generate numbers from 1 to 100
# It prints FizzBuzz if the number is cleanly divisible by 3 and 5
# It prints Fizz if cleanly divisible by 3 only
# It prints Buzz if cleanly divisible by 5 only
# Else it prints the number

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
