'''Exercise 7: Count the Number of Digits in a Number

Problem Statement:
Write a program that takes an integer `n` as input and counts the number of digits in `n` using recursion. Assume that `n` is a non-negative integer.
'''

'''def digits(n):
    if n == 0:
        return 0
    return 1 + digits(n // 10)


# start - end
# n = 1357, tổng = 0

# 135, tổng = 7
# 13, tổng = 7 + 5
# 1, tổng = 7 + 5 + 3
# 0, tổng = 7 + 5 + 3 + 1
# Dừng đệ quy

# 1357, count = 0
# 135, count = 1 -> mỗi lần gọi, sẽ tăng biến đếm lên 1 và đồng thời chia số đó cho 10 lấy phần nguyên
# 13, count = 2
# 1, count = 3
# 0, count = 4
# Dừng đệ quy
n = int(input("nhap n: "))
print(digits(n))
'''

'''
def sumdigits(n):
    # end: điềy kiện dừng trong đệ quy
    if n == 0:
        return 0
    """
    elif n > 0:
        return n // 10
    """
    return n % 10 + sumdigits(n // 10)


n = int(input("nhap so n: "))
"""
for i in range(n, 0, n // 10):
    sum = sum + n % 10
"""
print(sumdigits(n))
'''

'''Exercise 8: Determine the Largest Digit

Problem Statement:
Write a program that takes an integer `n` as input and determines the largest digit in `n` using recursion. Assume that `n` is a non-negative integer.
'''
'''

def findmax(n):
    max = 0
    if len(n) == 1:
        return max
    else:
        if n % 10 > max:
            max = n % 10

        return findmax(n // 10)


n = (input("nhap n: "))  # str: "13597", max = 0
# "1359", max = '7'
# "135", max = '9'
# len = 0
print(findmax(n))
''''''
String - vòng lặp for:"""
n = input("nhap n: ")  # n: 13597
maxNum = n[0]  # '1'
for i in n:
    # '1'      '3' '5' '9' '7'
    # max              ->
    # Cầm max đi so sánh với chữ số hàng chục, trăm, nghìn ,chục nghìn -> số nào > max hiện tại thì số đó là max
    if maxNum < i:
        maxNum = i

print(maxNum)'''

'''
Question 1: Merge Multiple Dictionaries with Summed Values
Description:
Merge a list of dictionaries by summing the values of common keys.
'''
'''list_of_dicts = [
    {'apple': 2, 'banana': 3},
    {'banana': 2, 'cherry': 5},
    {'apple': 1, 'cherry': 2, 'date': 4}
]
dict = {}
# Kiểm tra key này đã xuất hiện trong dict này hay chưa -> 'apple': 2
# dict = {'apple': 2}

# +1 vào value của nó
for i in list_of_dicts:
    # print(i)  # 1 dict
    for j in i:
        if j in dict:
            dict[j] += i.get(j)
        else:
            dict[j] = i.get(j)
print(dict)

"""
list = [Java Python C++ C++ C++ Python Python]
Java: 1 
Python: 3
C++: 3
dict={}
for key in list:
    if key in dict:
        dict[key]+=1
    else:
        dict[key]=1
        
"""

"""Question 3: Find Keys with Maximum Values
Description:
Identify all keys in a dictionary that have the maximum value.
Example:
'''

'''scores = {'Alice': 88, 'Bob': 95, 'Charlie': 95, 'David': 90}
maxvalue = []
value = []
for j in scores.values():
    value.append(j)
print(max(value))

for k, v in scores.items():
    if v == max(value):
        maxvalue.append(k)
print(maxvalue)
'''
'''Question 7: Find the Intersection of Dictionaries Based on Keys and Values
Description:
Find keys that exist in all dictionaries with the same corresponding values.'''
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 100, 'b': 250, 'd': 300}
dict3 = {'a': 100, 'c': 300, 'd': 400}
value = {}
for i in dict1:
    for j in dict2:
        for h in dict3:
            if i == j == h:
                value[i] = dict1.get(i)
print(value)
"""
print(value[0])
# Lấy value từ key:
print(dict1[value[0]])
# dictName.get("key")
print(dict1.get(value[0]))
"""
