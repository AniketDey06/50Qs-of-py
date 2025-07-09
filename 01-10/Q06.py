# Write a program to input three numbers (positive or negative). If they are unequal then display the
# greatest number otherwise, display they are equal. The program also displays whether the numbers
# entered by the user are 'All positive', 'All negative' or 'The combination of both'

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a==b==c:
    print("They are equal")
else:
    print("Greatest number is -", max(a,b,c))

if a>0 and b>0 and c>0:
    print("All positive")
elif a<0 and b<0 and c<0:
    print("All negative")
else:
    print("The combination of both")

# Code Compiled By - Aniket Dey