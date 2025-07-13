# Write a program to enter two numbers and check whether they are co-prime or not.
# Sample Input: 14, 15
# Sample Output: They are co-prime.

import math

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

gcd = math.gcd(num1, num2)

if(gcd == 1):
    print("They are co-prime")
else:
    print("They are not co-prime")


# Code Compiled By - Aniket Dey