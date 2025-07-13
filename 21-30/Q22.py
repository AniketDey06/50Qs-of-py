# Write a program in Java to find the sum of the series, taking the value of 'a' and 'n' from the user.
# s = 1 + a^2/1! + a^3/2! + .... + a^n+1/n!

import math

a = int(input("Enter num of a: "))
n = int(input("Enter num of n: "))

sum_series = 1

for i in range(1, n+1):
    num = a**(i+1) / math.factorial(i)
    sum_series += num

print("Sum of series is -", sum_series)

# Code Compiled By - Aniket Dey