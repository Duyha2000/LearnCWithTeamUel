# hàm đệ quy:

# For - while:

# Tính tổng các số từ 1 đến N:
"""
def sumNumer(N: int) -> int:
    sum = 0
    for i in range(N, 0, -1):
        sum += i
    return sum


# start - end - step
print(sumNumer(5))

# Hàm đệ quy:
"""
"""
def sumNumber(N: int) -> int:
    # B2: Phần cơ sở ( điều kiện để dừng đệ quy): end 
    if condition:
        # Điều kiện dừng
        pass
    # B1: Thực Hiện gọi đệ quy
    return ... +-* sumNumer(N - step)
"""


def sumRecursion(N: int) -> int:
    # B2: Điều kiện dừng: giống giá trị end của vòng lặp for
    if N == 0:
        return 0
    # B1: Xác định được quy luật của dãy số: Khi nhập n = 5: 5 4 3 2 1 (gọi đệ quy)
    # N - 1: start - step:
    # Tham số trong hàm đệ quy sẽ là start và step
    return N + sumRecursion(N - 1)


# UIT - Bkhoa: cấu trúc dữ liệu giải thuật:
# Với N = 5:
"""
 5 +  sumRecursion(4)
 5 + 4 +  sumRecursion(3)
 5 + 3 + 2 +  sumRecursion(2) 
 5 + 4 + 3 + 2 +  sumRecursion(1) 
 5 + 4 + 3 + 2 + 1 +  sumRecursion(0)
 --
 5 + 4 + 2 + 1 + 0 +  sumRecursion(-1)
 ---                - 1
"""

print(sumRecursion(5))


# Tính giai thừa: Nhập N và tính giai thừa số đó
# Input: 5
# Output: 5! = 5 * 4 * 3 * 2 * 1
# Những giá trị input (có thể thay đổi được, chính là tham số parameter trong hàm)
def factorial(N: int) -> int:
    product = 1
    for i in range(N, 0, -1):
        product *= i
    return product


# Sang đệ quy:
def factorialRecursion(N: int) -> int:
    # B2: Điều kiện dừng: (N = 1)
    if N == 1:
        return 1
    # B1: Xác định quy luật dãy số (phần đệ quy)
    # start .... step
    # N - 1
    return N * factorialRecursion(N - 1)


print(factorialRecursion(5))


# Cho 1 số N nhập từ bàn phím, tính tổng các số lẻ > 0 từ 1 đến N:
# Input: 8 (8 7 6 5 4 3 2 1 ...)
# 8 -> 1 ( 0 -1 )
# Output: 7 + 5 + 3 + 1  = 16
def sumOddNumber(N: int) -> int:
    # B2: Điều kiện dừng đệ quy:
    if N == 1:
        return 1

    # B1: Xác định quy luật dãy số:
    if N % 2 == 0:
        return sumOddNumber(N - 1)
    return N + sumOddNumber(N - 1)


print(sumOddNumber(8))

"""
Tháp hà nội:
n: số đĩa cần chuyển
a: cột gốc
b: cột trung gian
c: cột đích
"""


# số đĩa, gốc, trung gian, đích
def thapHaNoi(n, a, b, c):
    # Điều kiện dừng:
    if n == 1:
        print(f"{a} -> {c}")
    else:
        # Phần đệ quy:
        # Giả sử có 3 đĩa (n = 4)
        # B1: Chuyển 3 đĩa từ A sang B, đĩa C là đĩa trung gian
        thapHaNoi(n - 1, a, c, b)
        # B2: Chuyển 1 đĩa từ A sang C, B là đĩa trung gian
        thapHaNoi(1, a, b, c)
        # B3: Chuyển 3 đĩa từ B sang C, đĩa A sẽ làm đĩa trung gian
        thapHaNoi(n - 1, b, a, c)


n = 4
a = 'A'
b = 'B'
c = 'C'
print(thapHaNoi(n, a, b, c))
