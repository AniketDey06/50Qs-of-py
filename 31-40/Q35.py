# Write a program to accept a number and check whether the number is Automorphic or not.
# Automorphic number: (Automorphic number is the number, which is contained in the last digit(s) of its
# square.)
# Example: 25 is an Automorphic number as its square is 625 and 25 is present as the last two digits.

num = int(input("Enter a number: "))
square = num ** 2

num_str = str(num)
square_str = str(square)

if square_str.endswith(num_str):
    print(f"{num} is an Automorphic number.")
else:
    print(f"{num} is not an Automorphic number.")

# Code Compiled By - Aniket Dey