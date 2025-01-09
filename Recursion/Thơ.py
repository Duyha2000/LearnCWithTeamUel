""" Exercise 1: Calculate the Sum of Numbers from 1 to n

Write a program that takes an integer input `n` and calculates the sum of all numbers from 1 to `n` using recursion.
Input: 10, Output: 55

def sum_recursion(n):
    if n == 0:
        return 0
    return n + sum_recursion(n - 1)


n = int(input("Nhap input n:"))
if n >= 1:
    print(f"Sum of numbers from 1 to {n} is {sum_recursion(n)}")
else:
    print("Enter positive int")"""

"""Exercise 2: Calculate the Factorial of a Number
Write a program that takes an integer `n` as input and calculates 
the factorial of that integer using recursion.

Input: 5, Output: 120

def factorial_recursion(n):
    if n == 1:
        return 1
    return n * factorial_recursion(n - 1)


n = int(input("Nhap input n:"))
if n >= 1:
    print(f"Factorial of {n} is {factorial_recursion(n)}")
else:
    print("Enter positive int")"""

"""Exercise 3: Calculate the Sum of Odd Numbers

Given an integer `n` entered from the keyboard, write a recursive function 
that returns the sum of all positive odd numbers from 1 to `n`.

Input: 10, output: 25
(Explanation: 1 + 3 + 5 + 7 + 9 = 25)

def sum_odd(n):
    if n == 1:
        print(1, end=' ')
        return 1
    elif n % 2 == 0:
        return sum_odd(n - 1)
    else:
        print(n, end=' ')
        return n + sum_odd(n - 1)


n = int(input("Nhap input n:"))
if n > 0:
    print(f"Odd numbers from 1 to {n} are:")
    print(sum_odd(n))
    result = sum_odd(n)
    print(f"Sum of odd numbers from 1 to {n} is {result}")
else:
    print("Enter positive int")"""

"""Exercise 4: Fibonacci Sequence
- Base Cases:
  - F₀ = 0
  - F₁ = 1
- Recursive Formula:
  - Fₙ = Fₙ₋₁ + Fₙ₋₂, for n > 1

Input:10, output:55

def fibo_recursion(n):
    if n <= 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


n = int(input("Nhap STT fibo: "))
print(fibo_recursion(n))"""

"""Exercise 5: Natural Exponents
Write a program that takes two integers, `base` and `exponent`, 

Input:
2 10
Output: 1024 (2^10=1024)

def expo(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * expo(a, b - 1)


a = int(input("Enter base: "))
b = int(input("Enter expo: "))
print(expo(a, b))"""

"""Exercise 6: Calculate the Sum of Array Elements Recursively

Input:
5
1 2 3 4 5

Output: 15

list = []
for i in range(5):
    n = int(input("Nhap 5 so: "))
    list.append(n)


def sum_list(list):
    if not list:
        return 0
    return list[0] + sum_list(list[1:])


print(f"Total sum is: {sum_list(list)}")"""

"""Exercise 7: Count the Number of Digits in a Number
input 12345 --> output : 5

def num_of_digits(n):
    if 0 <= n < 10:
        return 1
    return 1 + num_of_digits(n // 10)

n = int(input("Enter a positive int: "))
print(f"Number of digits is: {num_of_digits(n)}") """

"""
Exercise 8: Determine the Largest Digit
Write a program that takes an integer `n` as input and determines the largest digit in `n` 
using recursion. Assume that `n` is a non-negative integer.

Input: 29483 <-
Output: 9
"""
# n = 29483
"""
while True:

    # B1: Lấy chữ số hàng đơn vị: 3, cho giá trị này là max, so sánh với từng chữ số
    # 29483 -> làm thế nào lấy ra được số 3: 29483 % 10 = 3 -> max (max = 3)
    # Cầm max đi so sánh với chữ số hàng chục, trăm, nghìn ,chục nghìn -> số nào > max hiện tại thì số đó là max
    max = n % 10  # 3

    if n == 0:
        break
    # list: [1 3 5 8 4]
    #              ->
    # Gán phần tử lớn nhất max cho phần tử đầu tiên list[0]
    # Đi so sánh với các phần tử khác trong list, phần tử nào lớn hơn thì nó là max
nStr = str(n)  # "29483"
maxNum = nStr[0]
for c in nStr:
    # c = '2' '9' '4' '8' '3'
    if maxNum < c:
        maxNum = c
print(maxNum)


def largest_digit(n):
    if n < 10:
        return n

    the_rest = largest_digit(n // 10)
    return max(n % 10, the_rest)


n = int(input("Enter a positive int: "))
print(f"The largest digit is: {largest_digit(n)}")"""

"""
Exercise 9: Enter a Number N and Calculate the Sum of Its Digits
Write a program that takes an integer `N` as input and calculates the sum of its digits using recursion.

Input:1234
Output: 10

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

n = int(input("Enter a number: "))
print(f"Sum of digits = {sum_digits(n)}")"""

"""
Exercise 11: Calculate the Sum of Consecutive Natural Squares
Write a program that takes an integer `n` as input and calculates the sum 
of the squares of the first `n` natural numbers using recursion.

Input:3
Process: 3^2 + 2^2 + 1^2 
Output:14

def sum_cs(n):
    if n == 1:
        return n
    return n ** 2 + sum_cs(n - 1)

n = int(input("Enter a number: "))
print(f"Sum of consecutive squares = {sum_cs(n)}")"""

"""
Exercise 13: Print the Array from Right to Left

Write a program that takes an array of `n` integers as input and prints the elements of the array 
from right to left using recursion.
Input: 5
1 2 3 4 5
Output: 5 4 3 2 1
"""


def rtol(n):
    if n == 0:
        return
    rtol(n - 1)
    print(n, end=' ')


n = int(input("Enter a number: "))
rtol(n)
