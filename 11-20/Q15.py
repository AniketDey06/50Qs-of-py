# WAP to calculate and display the fifty 'Prime Numbers' from a given number entered by the user

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number - "))
primes = []

while len(primes) < 50:
    if is_prime(num):
        primes.append(num)

    num+=1

print(primes)

# Code Compiled By - Aniket Dey