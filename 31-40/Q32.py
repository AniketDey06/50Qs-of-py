# Write a program to accept two numbers and find the Lowest Common Multiple (LCM) of the numbers.
# Hint: LCM = Product of two numbers/HCF

def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

hcf = find_hcf(num1, num2)
lcm = (num1 * num2) // hcf

print(f"LCM of {num1} and {num2} is {lcm}")

# Code Compiled By - Aniket Dey