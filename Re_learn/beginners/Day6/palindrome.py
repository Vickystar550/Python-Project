"""This program test for a Palindrome"""

# Prompt user for an input:
usr_input = input("Enter any string\n").replace(" ", "")


# Define a function that will check if the word is a palindrome:
def is_palindrome(string):
    """This checks if a string is a palindrome"""
    return string == string[::-1]


def checker(usr_input):
    """This function removes an element from its argument, and returns
    a modified string with the removed element as a tuple."""
    new_string = ""
    outcast = ""
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
    # create a variable s to store the result from the function checker()
    # remember s is a tuple
    s = checker(usr_input)

    # create a list to hold the removed elements. Append the last element in s to it.
    removed_list = []
    removed_list.append(s[-1])

    while not is_palindrome(s[0]): # if this is obey
        # reassign s to the result of checker() of the previous s[0]..:
        s = checker(s[0])
        # append the last element of this reassigned s to removed_list:
        removed_list.append(s[-1])

    # join the elements in removed_list to form a string:
    removed_string = ("".join(removed_list)).upper()
    # the new (suppose) palindrome must be the first element of s after the while loop is done executing:
    new_palindrome = s[0].upper()

    # Check for the new (supposed) palindrome length:
    # From research, a palindrome has a minimum length of 3: 
    if len(s[0]) < 3:
        # if the length of s[0] is <= 2, then the usr_input cannot be a palindrome
        print(f"{usr_input}, does not form a PALINDROME")
    else:
        # a palindrome is formed, congratulations!!
        print(f"The removed string is: {removed_string}, and the new Palindrome is: {new_palindrome}")