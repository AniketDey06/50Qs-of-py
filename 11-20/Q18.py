# Write a program in python to enter a number and check whether the number is a Palindrome or not 

num = str(input("Enter the number: "))

reversed_num = num[::-1]

if num==reversed_num:
    print("The number is Palindrom");
else:
    print("The number is not Palindrom");

# Code Compiled By - Aniket Dey