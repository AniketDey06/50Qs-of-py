# Write a program to accept a number and dispSamplelay the sum of its digits.
# Input: 542
# Sample Output: 5 + 4 + 2 = 11

num = int(input("Enter a num: "))
sum_of_digi = 0

while num>0:
    sum_of_digi += num % 10
    num = int(num/10)

print(sum_of_digi)

# Code Compiled By - Aniket Dey