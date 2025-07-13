# Write a program to find the factors of a number including 1 and the number itself.
# Sample Input: 18
# Sample Output: 1, 2, 3, 6, 9, 18

factors = []
num = int(input("Enter a num: "))
factors.append(1)

for i in range(2, int((num/2)+1)):
    if(num%i == 0):
        factors.append(i)

factors.append(num)
print(factors)

# Code Compiled By - Aniket Dey