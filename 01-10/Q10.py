# Write a program to accept 10 different numbers. Display the greatest and the smallest numbers from a
# set of numbers entered By user

max = 0
min = 0
i = 1

while (i<=10):
    num = int(input(f'{i} - Enter a Number : '))

    if(num > max):
        max = num
    
    if(num<min):
        min = num
    i+=1
    
print("Greatest Number is : ", max)
print("Smallest Number is : ", min)

# Code Compiled By - Aniket Dey