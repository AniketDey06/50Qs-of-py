# WAP to find the sum 'n' from the user. of series, taking the values of 'a' and
# S= a/2 + a/3 + a/4 +........a/n

a = int(input("Enter the value of a: "))
n = int(input("Enter the value of n (must be greater than 1): "))

if n <= 1:
    print("n must be greater than 1")
else: 
    sum_of_series = 0
    for i in range(2, n + 1):
        sum_of_series += a / i

    print(f"The sum of the series is: {sum_of_series}")

# Code Compiled By - Aniket Dey