# Write a program to input the length and breadth of a rectangle. Calculate and display the area, perimeter or diagonal of the rectangle as per the User's choice.

import math

l = float(input("Enter Lenght: "))
b = float(input("Enter Breadth: "))

print('What you would Like to Calculate: ')
print('[1]. Area')
print('[2]. Perimeter')
print('[3]. Diagonal')

ch = int(input("Enter Your Choice - "))

match ch:
    case 1:
        print("Area Is -",l*b)
    case 2:
        print("Perimeter Is - ", 2*(l+b))
    case 3:
        print("Diagonal Length Is - ", math.sqrt(l**2 + b**2))
    case default:
        print("something")

# Code Compiled By - Aniket Dey