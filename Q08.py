# Write a program to accept two numbers and find the Greatest Common Divisor (G.C.D) of two
# numbers. (HCF).

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD is ", gcd)

# Code Compiled By - Aniket Dey