# Write a program to accept a number and check whether the number is perfect or not. A number is said
# to be perfect, if the sum of the factors (including 1 and excluding the number itself) is same as the
# original number.

num = int(input("Enter a number - "))
sum = 0
for i in range(1, num):
    if(num%i == 0):
        sum = sum + i

if(sum == num):
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect Number.")

# Code Compiled By - Aniket Dey