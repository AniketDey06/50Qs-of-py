# Write a program to accept a number and display the new number after removing all zeros.
# Sample Input: 5400207
# Sample Output: 5427

num = input("Enter a number: ")

new_num = ""

for digit in num:
    if digit != 0:
        new_num += digit

print("New number:", new_num)

# Code Compiled By - Aniket Dey