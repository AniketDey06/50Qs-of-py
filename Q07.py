# Write a program to accept a number and check whether the number is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# Code Compiled By - Aniket Dey
