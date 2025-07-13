# WAP in py to accept nummber and display the frequency of each digit present in the number.

num = input("Enter a Number: ")
freq = {}

for key in num:
    if key in freq:
        freq[key] += 1
    else:
        freq[key] = 1

print(freq)

# Code Compiled By - Aniket Dey