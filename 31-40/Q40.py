# Write a py program to complete and display the sum of the following series.
# s = 1/2 + 2/3 + 3/4 + ....+ n

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num+1):
    sum += i/(i+1)

print(sum)

# Code Compiled By - Aniket Dey