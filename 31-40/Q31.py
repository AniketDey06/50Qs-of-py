# A number is said to be Unique if digits of a number are not repeated in it. Write a program to accept a
# number and check whether the number is Unique or not. The program displays the message
# accordingly.
# Sample Input: 5463
# Sample Output: It is a unique number.
# Sample Input: 3272
# Sample Output: It is not a unique number.

f = 0

num = input("Enter a Number: ")
freq = {}

for key in num:
    if key in freq:
        freq[key] += 1
        print("not unique")
        f=1
        break
    else:
        freq[key] = 1

if f==0:
    print("Number is unique")

# Code Compiled By - Aniket Dey