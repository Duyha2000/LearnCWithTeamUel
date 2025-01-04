"""Exercise 1: Calculate the Sum of Numbers from 1 to n

Problem Statement:
Write a program that takes an integer input `n` and calculates the sum of all numbers from 1 to `n` using recursion.

Input:
10

Output:
55"""


def sumNumber(N: int):
    if N == 1:
        return 1
    return N + sumNumber(N - 1)


print(sumNumber(10))

"""Exercise 2: Calculate the Factorial of a Number

Problem Statement:
Write a program that takes an integer `n` as input and calculates the factorial of that integer using recursion.

Input:
5
Output:
120

Input Description:
- A single integer `n` (0 ≤ n ≤ 20) representing the number to calculate the factorial of.

Output Description:
- A single integer representing the factorial of `n`.

Example:

Input:
3
Output:
6
"""


# sai kieu du lieu N: ủa là sao anh


def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N - 1)


print(factorial(3))

"""Exercise 3: Calculate the Sum of Odd Numbers

Problem Statement:
Given an integer `n` entered from the keyboard, write a recursive function that returns the sum of all positive odd numbers from 1 to `n`.

Input:
10

Output:
25
(Explanation: 1 + 3 + 5 + 7 + 9 = 25)

Input Description:
- A single integer `n` (1 ≤ n ≤ 10^6) representing the upper bound.

Output Description:
- A single integer representing the sum of all positive odd numbers from 1 to `n`.

Example:

Input:
7

Output:
16
(Explanation: 1 + 3 + 5 + 7 = 16)"""


def SumOddNumber(N):
    if N == 0:
        return 0
    if N % 2 == 0:
        return SumOddNumber(N - 1)
    return N + SumOddNumber(N - 1)


print(SumOddNumber(7))

"""Exercise 4: Fibonacci Sequence

Problem Statement:
Write a program that takes an integer `n` as input and calculates the `n`-th Fibonacci number using recursion. The Fibonacci sequence is defined as follows:

- Base Cases:
- F₀ = 0
- F₁ = 1
- Recursive Formula:
- Fₙ = Fₙ₋₁ + Fₙ₋₂, for n > 1

Input:
10

Output:
55

Input Description:
- A single integer `n` (0 ≤ n ≤ 50) representing the position in the Fibonacci sequence.

Output Description:
- A single integer representing the `n`-th Fibonacci number.

Example:

Input:
5

Output:
5"""


def Fibonacci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return Fibonacci(N - 1) + Fibonacci(N - 2)


print(Fibonacci(10))

"""Exercise 5: Natural Exponents

Problem Statement:
Write a program that takes two integers, `base` and `exponent`, and calculates the value of `base` raised to the power of `exponent` using recursion. Both `base` and `exponent` are non-negative integers.

Input:
2 10

Output:
1024

Input Description:
- Two space-separated integers:
- `base` (0 ≤ base ≤ 1000)
- `exponent` (0 ≤ exponent ≤ 20)

Output Description:
- A single integer representing the result of `base` raised to the power of `exponent`.

Example:

Input:
3 4

Output:
81"""


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print(power(3, 4))

"""Exercise 6: Calculate the Sum of Array Elements Recursively

Problem Statement:
Given an array of `n` integers, write a recursive function to calculate the sum of its elements.

Input:
5
1 2 3 4 5

Output:
15

Input Description:
- The first line contains an integer `n` (1 ≤ n ≤ 10^5), the number of elements in the array.
- The second line contains `n` space-separated integers representing the array elements.

Output Description:
- A single integer representing the sum of the array elements.

Example:

Input:
3
10 20 30

Output:
60"""

"""Exercise 7: Count the Number of Digits in a Number

Problem Statement:
Write a program that takes an integer `n` as input and counts the number of digits in `n` using recursion. Assume that `n` is a non-negative integer.

Input:
12345

Output:
5

Input Description:
- A single non-negative integer `n` (0 ≤ n ≤ 10^18).

Output Description:
- A single integer representing the number of digits in `n`.

Example:

Input:
0

Output:
1

---

Exercise 8: Determine the Largest Digit

Problem Statement:
Write a program that takes an integer `n` as input and determines the largest digit in `n` using recursion. Assume that `n` is a non-negative integer.

Input:
29483

Output:
9

Input Description:
- A single non-negative integer `n` (0 ≤ n ≤ 10^18).

Output Description:
- A single integer representing the largest digit in `n`.

Example:

Input:
56789

Output:
9

---

Exercise 9: Enter a Number N and Calculate the Sum of Its Digits

Problem Statement:
Write a program that takes an integer `N` as input and calculates the sum of its digits using recursion.

Input:
1234

Output:
10

Input Description:
- A single integer `N` (0 ≤ N ≤ 10^18).

Output Description:
- A single integer representing the sum of the digits of `N`.

Example:

Input:
999

Output:
27

---

Exercise 10: Calculate the Sum of the Sequence 1

Problem Statement:
Write a program that takes an integer `n` as input and calculates the sum of the sequence where each term is `1`. The sequence length is `n`. Use recursion to compute the sum.

Input:
5

Output:
5

Input Description:
- A single integer `n` (1 ≤ n ≤ 10^6) representing the number of terms in the sequence.

Output Description:
- A single integer representing the sum of the sequence.

Example:

Input:
10

Output:
10

---

Exercise 11: Calculate the Sum of Consecutive Natural Squares

Problem Statement:
Write a program that takes an integer `n` as input and calculates the sum of the squares of the first `n` natural numbers using recursion.

Input:
3

Output:
14

Input Description:
- A single integer `n` (1 ≤ n ≤ 10^4) representing the number of natural numbers to square and sum.

Output Description:
- A single integer representing the sum of the squares of the first `n` natural numbers.

Example:

Input:
5

Output:
55
(Explanation: 1² + 2² + 3² + 4² + 5² = 55)

---

Exercise 12: Calculate the Sum of Even Numbers in an Array

Problem Statement:
Given an array of `n` integers, write a program to calculate the sum of all even numbers in the array using recursion.

Input:
6
1 2 3 4 5 6

Output:
12

Input Description:
- The first line contains an integer `n` (1 ≤ n ≤ 10^5), the number of elements in the array.
- The second line contains `n` space-separated integers representing the array elements.

Output Description:
- A single integer representing the sum of all even numbers in the array.

Example:

Input:
4
7 8 9 10

Output:
18
(Explanation: 8 + 10 = 18)

---

Exercise 13: Print the Array from Right to Left

Problem Statement:
Write a program that takes an array of `n` integers as input and prints the elements of the array from right to left using recursion.

Input:
5
1 2 3 4 5

Output:
5 4 3 2 1

Input Description:
- The first line contains an integer `n` (1 ≤ n ≤ 10^4), the number of elements in the array.
- The second line contains `n` space-separated integers representing the array elements.

Output Description:
- A single line containing the array elements printed from right to left, separated by spaces.

Example:

Input:
3
10 20 30

Output:
30 20 10"""
