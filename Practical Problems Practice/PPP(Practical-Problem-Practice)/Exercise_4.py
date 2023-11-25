# Write a function called count_primes() that requires a single numeric argument. This function must display on the screen how many prime numbers there are in the range from zero to that number included, and then return the number of prime numbers found.


def count_primes(max_number):
    primes = set()  # Create an empty set to store prime numbers
    prime_count = 0  # Initialize a counter for prime numbers

    for number in range(2, max_number + 1):
        is_prime = True  # Initialize a flag to check if a number is prime
        # Check for divisors up to the square root of the number
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                is_prime = False  # If a divisor is found, the number is not prime
                break

        if is_prime:  # If the number is prime, add it to the set and increment the counter
            primes.add(number)
            prime_count += 1
    # Display the number of prime numbers found
    print("There are", prime_count, "prime numbers from 0 to", max_number)

    return prime_count  # Return the number of prime numbers found


prime_count = count_primes(100)
print("Total prime numbers:", prime_count)
