# Write a program to enter a number and check whether the number is 'Neon' or not. A number is said to
# be 'Neon', if sum of the digits of square of a number is equal to the number itself.
# Sample Input: 9
# Sample Output: 9*9 = 81, 8 + 1 = 9
# : 9 is a Neon number.

number = int(input("Enter a number: "))

sqnum = number*number
sumdig = 0

while sqnum > 0:
    sumdig = sqnum%10
    sqnum = int(sqnum/10)

if(sqnum == number):
    print("It is Neon Number")
else:
    print("It is not a Neon Number")

# Code Compiled By - Aniket Dey