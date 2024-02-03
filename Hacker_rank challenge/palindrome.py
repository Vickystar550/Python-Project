"""This program test for a Palindrome"""

# Ask user for an input:
usr_input = input("Enter any string\n").replace(" ", "")


# Define a function that will only check for palindrome:
def is_palindrome(string):
    return string == string[::-1]

def checker(usr_input):
    new_string = ""
    outcast  = ""
    j = -1
    for i in usr_input:
        if i != usr_input[j]:
            outcast += i
            new_string = usr_input.replace(i, "", 1)
            break
        j -= 1
    return new_string, outcast


# START THE PROGRAM:
if is_palindrome(usr_input):
    print(f"{usr_input}, is a Palindrome")
else:
    s = checker(usr_input)

    removed_list = []
    removed_list.append(s[-1])

    while not is_palindrome(s[0]):
        s = checker(s[0])
        removed_list.append(s[-1])

    removed_string = ("".join(removed_list)).upper()
    new_palindrome = s[0].upper()

    if len(s[0]) <= 2:
        print(f"{usr_input}, does not form a PALINDROME")
    else:
        print(f"The removed string is: {removed_string}, and the new Palindrome is: {new_palindrome}")
        
