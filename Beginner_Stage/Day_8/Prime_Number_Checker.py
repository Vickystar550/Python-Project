# This program checks if a given number is a prime number:

n = int(input("Check this number:\n"))


def prime_checker(numb=n):
    # To be a prime number, n must be evenly divisible by 1 and itself only
    # this implies that the i intermediary numbers b/w 1 and n must return remainder on dividing n
    # Loop through 1 to n with lower and upper boundary exclusive
    is_prime = True
    for i in range(2, numb):
        if numb % i == 0:
            is_prime = False

    if is_prime:
        print("It\'s a prime number.")
    else:
        print("It\'s not a prime number.")


prime_checker()
