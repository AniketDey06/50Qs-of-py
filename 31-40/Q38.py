# Write a java program to complete and display the sum of the following series.
# 2-4+6-8+...........to n

num = int(input("Enter a number: "))
count = 1
sum = 0

for i in range(2, num+1, 2):
    if count%2 == 0:
        sum -= i
        count += 1
    else:
        sum += i
        count += 1

print(sum)

# Code Compiled By - Aniket Dey