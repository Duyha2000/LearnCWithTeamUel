'''Exercise 1: Calculate the Sum of Numbers from 1 to n

Problem Statement:
Write a program that takes an integer input `n` and calculates the sum of all numbers from 1 to `n` using recursion.
'''

'''def tong(N):
    if N == 0:
        return 0
    return N + tong(N - 1)


N = int(input("nhap so n: "))
print(tong(N))
'''
'''Exercise 2: Calculate the Factorial of a Number

Problem Statement:
Write a program that takes an integer `n` as input and calculates the factorial of that integer using recursion.
'''

'''def giaithua(n):
    if n == 1:
        return 1
    return n * giaithua(n - 1)


n = int(input("nhap so n: "))
print(giaithua(n))'''

'''Exercise 3: Calculate the Sum of Odd Numbers

Problem Statement:
Given an integer `n` entered from the keyboard, write a recursive function that returns the sum of all positive odd numbers from 1 to `n`.
'''

'''def tongsole(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return tongsole(n - 1)
    return n + tongsole(n - 1)


n = int(input("nhap so n: "))
print(f"tong cac so le tu 0 toi n la: {tongsole(n)}")

Exercise 4: Fibonacci Sequence

Problem Statement:
Write a program that takes an integer `n` as input and calculates the `n`-th Fibonacci number using recursion. The Fibonacci sequence is defined as follows:

- Base Cases:
- F₀ = 0
- F₁ = 1
- Recursive Formula:
-> Fₙ = "Fₙ₋₁ + Fₙ₋₂", for n > 1
'''

'''def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)


n = int(input("nhap so n: "))
print(fibo(n))
'''
'''Exercise 5: Natural Exponents

Problem Statement:
Write a program that takes two integers, `base` and `exponent`, and calculates the value of `base` raised to the power of `exponent` using recursion. Both `base` and `exponent` are non-negative integers.
'''

'''
def natural(n, m):
    if n == 1:
        return 1
    elif m == 1:
        return n
    return n * natural(n, m - 1)


n = int(input("nhap so base: "))
m = int(input("nhap so exponent: "))
print(natural(n, m))

Exercise 6: Calculate the Sum of Array Elements Recursively

Problem Statement:
Given an array of `n` integers, write a recursive function to calculate the sum of its elements.
'''
list = []
n = int(input("nhap so luong so can tinh: "))  # n = 5
for i in range(n):
    list.append(int(input(f"nhap so thu {i + 1} ")))


# sum = list[4] + list[3] + ... + list[0]
def sum(list, n):
    # B2: Điều kiện dừng đệ quy:
    if n == 1:
        return list[0]
    # B1: Quy luật của dãy: lùi từ list[4] -> về list[0]
    # 4 3 2 1 0
    return list[n - 1] + sum(list, n - 1)


print(sum(list, n))
