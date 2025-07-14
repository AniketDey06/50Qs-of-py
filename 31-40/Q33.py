# Write a program to accept two numbers and check whether they are twin prime or not.
# [Hint: Twin prime numbers are the prime numbers whose difference is two.
# e.g.: (5, 7), (11, 13)........

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if is_prime(num1) and is_prime(num2) and abs(num1 - num2) == 2:
    print("Twin Primes.")
else:
    print("NOT Twin Primes.")

# Code Compiled By - Aniket Dey