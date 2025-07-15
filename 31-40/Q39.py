# Write a java program to complete and display the sum of the following series.
# S=1!+2!+3!+4!+........+n!

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num+1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += fact

print(sum)

# Code Compiled By - Aniket Dey