# Write a py program to complete and display the sum of the following series.
# S= 1+2/1*2 + 1+2+3/1*2*3 + ...

import math

num = int(input("Enter a number: "))
i = 2

sum = 0

while i <= num:
    upper =  i * (i + 1) / 2
    lower = math.factorial(i)

    sum += upper/lower

    i += 1

print(sum)

# Code Compiled By - Aniket Dey