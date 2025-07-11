#  Using switch statement, write a menu driven program:
# ● To check and display whether a number input by the user is a composite number or not. 
# (A number is said to be a composite, if it has one or more than one factor excluding one and the
# number itself).
# Example: 4, 6, 8, 9
# ● To find the smallest digit of an integer that is input.
# Sample input: 6524
# Sample output: Smallest digit is 2.
# For an incorrect choice, an appropriate error message should be displayed

def composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2+1)):
        if n % i == 0:
            return True
    return False

def smallest(n):
    n = abs(n)
    smallest = 9
    while n > 0:
        digit = n % 10
        if digit < smallest:
            smallest = digit
        n = n // 10
    return smallest

print("1. Check Composite Number")
print("2. Find Smallest Digit in a Number")

choice = int(input("Enter your choice (1 or 2): "))

match choice:
    case 1:
        number = int(input("Enter a number: "))
        if composite(number):
            print(f"{number} is a Composite Number.")
        else:
            print(f"{number} is NOT a Composite Number.")
    case 2:
        number = int(input("Enter a number: "))
        result = smallest(number)
        print(f"Smallest digit is {result}.")
    case _:
        print("Invalid choice!")

# Code Compiled By - Aniket Dey