"""Exercise 0: Calculate the Sum from 1 to n
Problem: Enter a positive integer n and calculate the sum of numbers from 1 to n.

def sum(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum
n=int(input("Enter positive int: "))
print(sum(n))"""

"""Exercise 1: Calculate the Sum of Consecutive Natural Squares
Problem: Calculate the sum of squares of consecutive natural numbers from 1 to n.

def sumSquare(n):
    sum=0
    for i in range (1,n+1):
        sum+=i**2
    return sum
n=int(input("Enter positive int: "))
print(sumSquare(n))"""

"""Exercise 2: Sum of Digits of a Factorial
Problem: Enter a positive integer n, calculate its factorial, and find the sum of its digits.
n!
Example:
Input: Enter a positive integer n: 5
Output: Factorial of 5 is 120 Sum of digits of the factorial is: 3

n=int(input("Enter positive int: "))
def Factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact
# 120 -> 1 + 2 + 0
m= Factorial(n)
def sumDigits(m):
    sum=0
    while m>0:
        sum=sum+m%10
        m=m//10
    return sum
print(sumDigits(m))"""

"""
Exercise 7: Find the n-th Fibonacci Number
Problem: Calculate the n-th Fibonacci number.
Fibonacci: sum of the two preceding ones

def fibonacci (n):
    if n<=2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter positive int: "))
print(f"The {n}th Fibo number is {fibonacci(n)}")"""

"""Exercise 12: Check Palindrome Number
Problem: Check if a positive integer n is a palindrome (reads the same backward and forward).
--> Reversed
Input: Enter a positive integer n: 121
Output: 121 is a palindrome number

n=int(input("Enter a positive int:"))
def isCheckPalindrome(n): #-> bool:
    origin=n
    reversed=0
    while n>0:
        last_digit=n%10
        reversed= reversed*10+last_digit
        n=n//10
    return origin==reversed

if isCheckPalindrome(n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")"""

"""Exercise 13: Find the Greatest Common Divisor (GCD) and Largest Prime Factor
Problem: Find the greatest common divisor (GCD) of two numbers, decompose it into prime factors, and display the largest prime factor.
Input: Enter the first number: 48 Enter the second number: 60
Output: GCD of 48 and 60 is: 12 
Prime factor decomposition of 12: 2 * 2 * 3 Largest prime factor: 3
-> Hàm prime để check số nguyên tố
-> Xong lấy số 12 chia các số từ 2 -> 11, và số đấy là nguyên tố thì sẽ tìm được largest 
"""

a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
def gcd(a,b):
    gcd=1
    i=1
    while i in range (1,min(a,b)):
        if a%i==0 and b%i==0:
            gcd=i
        i=i+1
    return gcd
print(f"Greatest Common Divisor of {a} and {b} is {gcd(a,b)}")
n=gcd(a,b) # 12

def CheckPrime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

def lpf(n):
    lpf=1
    # 12: chia hết cho 1 số nguyên tố,
    # 1 -> 12
    for i in range (1,n+1):
        if CheckPrime(i) and n%i==0:
            lpf=i
    return lpf

print(f"Largest Prime Factor of {gcd(a,b)} is {lpf(n)}")
