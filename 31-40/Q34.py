# A number is said to be Duck if the digit zero is (0) present in it. Write a program to accept a number and
# check whether the number is Duck or not. The program displays the message accordingly. (The
# number must not begin with zero)
# Sample Input: 5063
# Sample Output: It is a Duck number.
# Sample Input: 7453
# Sample Output: It is not a Duck number.

num = input("Enter a number: ")

if num[0] == '0':
    print("The number must not begin with zero")
elif '0' in num[1:]:
    print("It is a Duck number.")
else:
    print("It is not a Duck number.")

# Code Compiled By - Aniket Dey