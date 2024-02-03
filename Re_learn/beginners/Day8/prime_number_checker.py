def prime_number_checker():
    """This function checks if a given number is a prime number"""
    number = int(input("Enter a positive integer:\n"))
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(f"\n{number} is a prime number") 
    else: 
        print(f"\n{number} isn't a prime number")

prime_number_checker()