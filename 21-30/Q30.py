# A prime number is said to be 'Twisted Prime', if the new number obtained after reversing the digits is
# also a prime number. Write a program to accept a number and check whether the number is 'Twisted
# Prime' or not.
# Sample Input: 167
# Sample Output: 761
# 167 is a 'Twisted Prime'

def rev_prime(num):
    temp_num = num
    rev_num = 0
    while(temp_num>0):
        digi = temp_num%10
        rev_num = rev_num*10 + digi
        temp_num = int(temp_num/10)

    if check_prime(rev_num):
        return True
    else: 
        return False
    

def check_prime(num):
    for i in range(2, int((num/2)+1)):
        if(num % i == 0):
            return False
    return True


num = int(input("Enter a Number: "))

if check_prime(num):
    if rev_prime(num):
        print("Twisted Prime")
    else: 
        print("not Twisted Prime")

else:
    print("Not prime. no checks farther")

# Code Compiled By - Aniket Dey