print("This program calculate both the sum of even and odd numbers from 1 to 100\n")

even = 0
odd = 0
for i in range(1, 101):
    if i % 2:
        even += i
    else:
        odd += i
print("\nSum of even is {}, while sum of odd is: {}".format(even, odd))