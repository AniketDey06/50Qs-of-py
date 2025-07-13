# Write a program to print the sum of negative numbers, sum of positive odd numbers and sum of
# positive even numbers from a list of numbers entered terminates when the user enters zero.

sum_of_negs = 0
sum_of_odds = 0
sum_of_eves = 0

while True:
    num = int(input("Enter a num (hit 0 exit): "))

    if num == 0:
        break

    if num > 0:
        if num%2 == 0:
            sum_of_eves += num
        else:
            sum_of_odds += num
    else:
        sum_of_negs += num

print(f"\nSum of negative numbers is {sum_of_negs}")
print(f"Sum of positive odd numbers is {sum_of_odds}")
print(f"Sum of positive even numbers is {sum_of_eves}")


# Code Compiled By - Aniket Dey