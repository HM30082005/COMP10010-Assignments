# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def primes_between_n_and_m(n, m):
#     primes = []
#     num = 2
#     while len(primes) < m:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes[n - 1:m]

# # Example usage
# n = int(input("Enter the value of n: "))
# m = int(input("Enter the value of m: "))
# prime_numbers = primes_between_n_and_m(n, m)
# print(f"The prime numbers between {n}th and {m}th prime numbers are: {prime_numbers}")

import random

def binary_search_guess_number(low, high, magic_number):
    attempts = 0
    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        if guess == magic_number:
            return guess, attempts
        elif guess < magic_number:
            print("Magic number is higher than", guess)
            low = guess + 1
        else:
            print("Magic number is lower than", guess)
            high = guess - 1

    return None, attempts

def main():
    low = 1
    high = 100  # You can change the range of the magic number as per your preference
    magic_number = random.randint(low, high)
    
    print("Welcome to the Guess the Number game!")
    print(f"Guess the magic number between {low} and {high}")

    guess, attempts = binary_search_guess_number(low, high, magic_number)

    if guess is not None:
        print(f"Congratulations! You guessed the magic number {magic_number} in {attempts} attempts.")
    else:
        print(f"Sorry! You couldn't guess the magic number {magic_number} in {attempts} attempts.")

if __name__ == "__main__":
    main()
