#Exercise 0: Calculate the Sum from 1 to n
"""def sum(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum
n=10
print (sum(n))"""

#Exercise 1: Calculate the Sum of Consecutive Natural Squares
"""def sum(n):
    sum=0
    for i in range (1,n+1):
        sum+=i**2
    return sum
n=4
print (sum(n))"""

#Exercise 2: Sum of Digits of a Factorial
""" n=int(input("Input the value of N:")
    def factorial(n):
        fact=1
        for i in range (n,n+1):
            fact*=i
        return factorial
    def sum_of_digits(n):
        S=0
        while n>0:
            S+=n%10
            n//=10
        return S
    print( sum_of_digits(n))
"""

#Exercise 3:  Find the Cube of a Number / Create a function to find the cube of a predefined number number = 5.
"""def cube_of_number(n):
        return n**3
    n=5
    print (cube_of_number(n))"""

#Exercise 4: Prime Number Check/Check if a positive integer n is a prime number.
"""def isPrime(n):
    if n<=1:
        return False
    for i in range (2,int(n**0,5)+1):
        if n%i==0:
            return False
    return True
    print (isPrime(5))"""

#Exercise 5: Sum of Digits of a Number/Calculate the sum of digits of a positive integer n.
""" def sum_of_digits(n):
        S = 0
        while n > 0:
            S += n % 10
            n //= 10
        return S
    n=456
    print (sum_of_digits(n))"""
#Exercise 6: Calculate Area and Circumference of a Circle
# Problem: Calculate the area and circumference of a circle with a given radius.
""" from math import pi
    def circle_area_and_circumference(radius):
        area = pi * radius ** 2
        circumference = 2 * pi * radius
        return area, circumference
    radius=7
    print (circle_area_and_circumference(radius))"""
# Exercise 7:  Find the n-th Fibonacci Number
# Problem: Calculate the n-th Fibonacci number.

def nth_fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        next_fib = a + b
        a = b
        b = next_fib
    return a if n == 0 else b
print(nth_fibonacci(7))
#Exercise 8: Calculate Power of a Number
# Problem: Calculate the power of a base number raised to an exponent.
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
print(power(2, 3))
#Exercise 9: Check Even or Odd Number
# Problem: Check if a positive integer n is even or odd.
def is_even(n):
    return n%2==0
n=10
if is_even(n):
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")
#Exercise 10: Check Perfect Number
def is_perfect_number(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n
n=6
if is_perfect_number(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
#Exercise 11:Reverse a Number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num
print(reverse_number(1234))
#Exercise 12:Check Palindrome Number
def is_palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num
n=121
if is_palindrome(n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
#Exercise 13: Find the Greatest Common Divisor (GCD) and Largest Prime Factor

