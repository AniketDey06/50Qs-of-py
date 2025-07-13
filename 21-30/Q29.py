# Write a program to accept a number and check whether the number is present in the Fibonacci series
# or not. The program displays the message accordingly.
# Sample Input: 55
# Sample output: 55 is present in the Fibonacci series.

f=0
num = int(input("Enter a Number: "))

n1 = 0
n2 = 1
for i in range (3, int(num+1)):
    n3 = n2 + n1
    n2 = n1
    n1 = i

    if(n3 == num):
        print("it is a fobo num")
        f = 1
        break

if f==0:
    print("it is not a fobo num")

# Code Compiled By - Aniket Dey