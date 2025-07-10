# You want to calculate the sum of all positive even numbers and the sum of all negative odd numbers
# from a set of numbers. You can enter 0 (zero) to quit the program and thus it displays the result. Write a
# program to perform the above task.

positive_even = 0
negative_odd = 0

while True:
    num = int(input('Enter a number (0 to quit): '))

    if num == 0:
        break

    if num > 0 and num % 2 == 0:
        positive_even += num
    elif num < 0 and num%2 !=0:
        negative_odd += num

print("Sum of positive even numbers:", positive_even)
print("Sum of negative odd numbers:", negative_odd)

# Code Compiled By - Aniket Dey