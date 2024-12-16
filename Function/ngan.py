# bài 0 Enter a positive integer n and calculate the sum of numbers from 1 to n.

'''def tinhtong(n):
    sum=0
    for i in range (1,n+1):
        sum +=i
    return sum
n=10
print(tinhtong(n))
'''

#Exercise 1:Calculate the sum of squares of consecutive natural numbers from 1 to n.

"""
def sumofsquares(n):
    sum=0
    for i in range (1,n+1):
        sum+=i**2
    return sum
n=4
print(sumofsquares(n))

#2: Enter a positive integer n, calculate its factorial, and find the sum of its digits.
n=int(input("nhap n: "))
def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact

m = factorial(n) # 120 ->while =>  %10, /10
def sumDigits(m):
    sum=0
    while m>0:
        sum=sum+m%10
        m=m//10
    return sum
print(sumDigits(m))

print(m)
"""
#3:Create a function to find the cube of a predefined number number = 5.
'''n=5
def cubeofnumber(n):
    cube=n**3
    return cube

print(cubeofnumber(n))'''

#4:Check if a positive integer n is a prime number.
'''n=int(input("nhap n: "))
def isprime(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
if isprime(n):
    print("so nguyen to")
else:
    print("khong phai so nguyen to")'''

#5:Calculate the sum of digits of a positive integer n.
'''def sumDigits(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum
n=int(input("nhap n: "))
print(sumDigits(n))'''

#6:Calculate the area and Calculate the area and circumference of a circle with a given radius.
'''n=int(input("nhap n: "))
def calArea(n):
    area=2*3.14*(n**2)
    return area
def calCircumference(n):
    circumference=2*3.14*n
    return circumference
print("area: ",calArea(n))
print("circumference: ",calCircumference(n))'''

#7:  Calculate the n-th Fibonacci number.
## F1 = 1 - F2 =1
## F3 = F1 + F2 = 2
## F4 = F3 + F2 = 2 + 1 = 3
## F5 = F4 + F3 = 3 + 2 = 5
## 5 -> gọi đến số F5 -> 5
#8:  Calculate the power of a base number raised to an exponent
n=int(input("nhap n: "))
def fibonacci(n):
    f1=1
    f2=1
    for i in range (1,n+1):

'''base=int(input("base: "))
expo= int(input("exponent: "))
def cal(base,expo):
    result=base**expo
    return result
print(cal(base,expo))
'''
#9:Check if a positive integer n is even or odd.
'''n=int(input("nhap n: "))
def isEven(n):
    if n%2==0:
        return True
    return False
if isEven(n):
    print(f"{n} la so chan")
else:
    print(f"{n} la so le")
'''

#10:: Check if a positive integer n is a perfect number (a number whose divisors' sum equals the number itself).
'''n=int(input("nhap n: "))
def perfect(n):
    sum=0
    for i in range (1,n):
        if n%i==0:
            sum+=i
    if sum == n:
        return True
# 6: 1 2 3 6
# sum = 1 + 2 + 3 = number = 6
if perfect(n):
    print(f"{n} la so hoan hao")
else:
    print(f"{n} khong la so hoan hao")
'''

#11: Find the reverse of a positive integer n.

#12: Check if a positive integer n is a palindrome (reads the same backward and forward).

#13:Find the greatest common divisor (GCD) of two numbers, decompose it into prime factors, and display the largest prime factor.
