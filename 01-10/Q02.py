# Write a program to enter three angles of a triangle and check whether a triangle is possible or not. If
# possible, then display whether it is an Acute- Angled triangle, a Right-Angled Triangle or an
# Obtuse-Angled Triangle otherwise, display 'Triangle is not possible'.


angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("It is an Acute-Angled Triangle")
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("It is a Right-Angled Triangle")
    else:
        print("It is an Obtuse-Angled Triangle")
else:
    print("Triangle is not possible")

# Code Compiled By - Aniket Dey