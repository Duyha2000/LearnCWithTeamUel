'''Bài 1: Đếm số lần xuất hiện của các phần tử
Đề bài: Đếm số lần xuất hiện của mỗi phần tử trong một danh sách.
lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
Kết quả:
{'apple': 3, 'banana': 2, 'orange': 1}'''

lst = ["apple", "banana", "apple", "orange", "banana", "apple"]

'''Bài tập 1: Tạo một dictionary với khóa kiểu int và giá trị kiểu string.
Thêm ít nhất 5 cặp khóa - giá trị vào dictionary. In ra giá trị của một khóa bất kỳ. In ra kích thước của dictionary.
'''
'''dict = {}
dict["1"] = "chuối"
dict["2"] = "táo"
dict["3"] = "vải"
dict["4"] = "quýt"
dict["5"] = "dưa"
dict["6"] = "nho"
print(dict)
print(len(dict))
print(dict["4"])
'''
'''Bài tập 2: Bài tập về Thêm và Xóa phần tử:
Tạo một dictionary với khóa kiểu char và giá trị kiểu int.
Thêm 3 phần tử vào dictionary. Xóa một phần tử bằng cách sử dụng hàm pop và in ra các phần tử trong mảng'''
'''dict2 = {
    "c": 1,
    "t": 2,
    "v": 3
}
dict2["q"] = 4
dict2["d"] = 5
dict2["n"] = 6
dict2.pop("t")
dict2.items()
for i, j in dict2.items():
    print(f"{i} : {j}")
'''
'''Bài tập 3: Tổng giá trị của các phần tử
Đề bài: Tính tổng giá trị của tất cả các phần tử trong một dictionary.
Input:
prices = {"apple": 3, "banana": 2, "orange": 5}

Output: 10
dict = {
    "chó": 23,
    "mefo": 30,
    "chuột": 10,
    "gà": 7,
}
sum = 0
for i in dict.values():
    sum += i
print("tổng các giá trị phần tử: ", sum)
'''

'''Bài tâp 4: Đếm tần suất xuất hiện của các số trong dãy và in ra kết quả
Input: 8 1 1 2 1 3 5 1 -4
Output:
-4 1
1 4
2 1
3 1
5 1'''
'''list = [8, 1, 1, 2, 1, 3, 5, 1, -4]
dict = {}
for item in list:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)'''

'''Bài tâp 5: Đếm tần suất xuất hiện của của mỗi chuỗi:
Input: Python Java PHP Python Javascript SQL SQL C++ C#
Output: C# 1
C++ 1
Java 1
Javascript 1
PHP 1
Python 2
SQL 2'''
'''list = ["Python", "Java", "PHP", "Python", "Javascript", "SQL", "SQL", "C++", "C#"]
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for j, k in dict.items():
    print(f"{j} : {k}")
'''

'''Bài 6. Tìm số xuất hiện nhiều lần nhất trong mảng:
Tìm từ xuất hiện nhiều nhất trong mảng, trong trường hợp có nhiều số có cùng số lần xuất hiện thì lấy số nhỏ nhất.
Ví dụ:
Input:
1 10 1 1 2 2 2
Output:
1

1: 3
2: 3
10: 1
'''

list = [1, 10, 1, 1, 2, 2, 2]
dict = {}
values = []
keys = []
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
for j in dict.values():
    values.append(j)
print(max(values))  # 3

# Vòng for (key,value) -> so sánh value với max(values): đẩy key vào list -> keys
for k, v in dict.items():
    if v == max(values):
        keys.append(k)
print(keys)
print(min(keys))
