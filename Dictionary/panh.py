"""Bài tập 1: Tạo một dictionary với khóa kiểu int và giá trị kiểu string.
Thêm ít nhất 5 cặp khóa - giá trị vào dictionary. In ra giá trị của một khóa bất kỳ. In ra kích thước của dictionary.

Input: Tran Duc Duy Tran Duc
Output: 1 - Tran
2 - Duc
3 - Duy
4 - Tran
5 - Duc 5"""

menu = {
    1: "bàn",
    2: "ghế",
    3: "sách",
    4: "bút",
    5: "thước"
}
for key in menu:
    print(f"{key}")
print("kích thước của dict là:", len(menu))

"""Bài tập 2: Bài tập về Thêm và Xóa phần tử:
Tạo một dictionary với khóa kiểu char và giá trị kiểu int.
Thêm 3 phần tử vào dictionary. Xóa một phần tử bằng cách sử dụng hàm pop và in ra các phần tử trong mảng
Input: A 10 B 20 C 30
Xóa B
Output: A - 10 C - 30"""

menu = {
    "A": 10,
    "B": 9,
    "C": 8,
}
menu["D"] = 7
menu["E"] = 6
menu["F"] = 5
remove_value = menu.pop("C")
print("Dictionary cuối cùng:", menu)

"""Bài tập 3: Tổng giá trị của các phần tử
Đề bài: Tính tổng giá trị của tất cả các phần tử trong một dictionary.
Input:
prices = {"apple": 3, "banana": 2, "orange": 5}

Output: 10"""

dict = {
    "apple": 3,
    "banana": 2,
    "orange": 5
}
total = sum(dict.values())
print("Tổng số lượng trái cây là:", total)

"""Bài tâp 4: Đếm tần suất xuất hiện của các số trong dãy và in ra kết quả
Input: 8 1 1 2 1 3 5 1 -4
Output:
-4 1
1 4
2 1
3 1
5 1"""

numbers = [8, 1, 1, 2, 1, 3, 5, 1, -4]
count_dict = {}
for item in numbers:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

for key, value in count_dict.items():
    print(key, value)

"""Bài tâp 5: Đếm tần suất xuất hiện của của mỗi chuỗi:
Input: Python Java PHP Python Javascript SQL SQL C++ C#
Output: C# 1
C++ 1
Java 1
Javascript 1
PHP 1
Python 2
SQL 2"""

string = ["Python", "Java", "PHP", "Python", "Javascript", "SQL", "SQL", "C++", "C#"]
count_dict = {}
for item in string:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

for key, value in count_dict.items():
    print(key, value)

"""Bài 6:Tìm số xuất hiện nhiều lần nhất trong mảng:
Tìm từ xuất hiện nhiều nhất trong mảng, trong trường hợp có nhiều số có cùng số lần xuất hiện thì lấy số nhỏ nhất.
Ví dụ:
Input:
1 10 1 1 2 2 2
Output:
1

1: 3
2: 3
10: 1
"""
num = [1, 10, 1, 1, 2, 2, 2]
count_dict = {}
for item in num:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Tuần suất xuất hiện của các số:", count_dict)
max_count = max(count_dict.values())  # 3
lst = []

# Vòng for (key,value) -> so sánh value với max_count: đẩy key vào 1
# cái list
for key, value in count_dict.items():
    if value == max_count:
        lst.append(key)
result = min(lst)
print("Số xuất hiện nhiều nhất và bé nhất trong mảng là:", result)
