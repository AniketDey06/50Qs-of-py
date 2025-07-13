# Write a program in Java to enter a number and check whether the number is an Armstrong or not.
# 21. A number is said to be an Armstrong, if the sum of cubes of digits is equal to the original number

sum_of_digit = 0

num = int(input("Enter the number: "))
temp_num = num

while temp_num>0:
    digit = temp_num % 10
    sum_of_digit += digit**3
    temp_num = int(temp_num / 10)

if(sum_of_digit == num):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')

# Code Compiled By - Aniket Dey