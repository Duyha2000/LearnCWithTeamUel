#  String:
"""
n = "hellllo"
# Chỉ số, chiều dài, duyệt String bằng vòng lặp for:
lst = [1,2,3,4,5] # -1
# Chỉ số:
print(n[0])
# chiều dài String:
print(len(n)) #
#m = int(input("Nhập m: "))
# Lấy ký tự cuối cùng trong String:
print(n[len(n)-1]) # o
# Duyệt string bằng vòng lặp for:
# for i in range: -> xử lý những bài tập liên quan chỉ số/ vị trí
# for i in n: -> từng ký tự trong chuỗi đấy
for i in n:
    print(i , end=" ")
# Nhập vào 1 ký tự, đếm xem ký tự đấy xuất hiện bao nhiêu lần trong chuỗi
l = input("Nhập vào 1 ký tự: ")
count = 0
for i in n:
    if i == l:
        count +=1
print(count) # 4 lần
print()
for i in range(len(n)):
    print(n[i], end=" ")
    # Các toán tử với chuỗi
s1 = "hello"
s2 = "World"
print(s1 + s2)  # Toán tử cộng chuỗi:
# Toán tử nhân chuỗi:
# In ra chữ hello 5 lần:
for i in range(5):
    print(s1)
print(s1 * 5)  # Ít dùng
# Toán tử "in": True/ False
print("he" in s1)  # True
print("heo" in s1)  # False
s3 = "   XInchao   "
# 1 số hàm xử lý chuỗi trong python:
print(s3.lower())  # Viết thường
print(s3.upper())  # viết hoa
print(s3.strip())  # Xóa khoảng trắng
# split:
s = "apple,banana,cherry"  # biến đổi string thành list:
lst = s.split(",")
print(lst)
s4 = " Hello  Python  3.10"
lst2 = s.strip().split()
print(lst2)
# replace(old, new):
s = "hello Python, Python is very easy"
newS = s.replace("Python", "Java")
print(newS)
# Ban đầu có 1 string là: H3344o -> thay đổi số 3 và số 4 thành Heello
str = "H3344o"
newStr2 = str.replace("3", "e").replace("4", "l")  # thay đổi tất cả ký tự cũ -> sang ký tự mới
print(newStr2)  # Hee44o
m = input().strip().lower()
print(m)
# isalpha - islower - isupper - isdigit: true / false:
# slicing: [start, end, step]
# start: 2 end 5 -> 2,3,4 -> lấy đầu, bỏ đuôi
# step > 0 -> đi từ trái qua phải, step < 0 thì đi từ phải qua trái:
#  Set: cũng là 1 list: chỉ chứa những phần tử không trùng lặp
# khởi tạo set: {}
mySet = {1, 2, 3, 1, 2, 3}  # set sẽ loại bỏ những phần tử trùng lặp:
print(mySet)  # {1, 2, 3}
# Không có khái niệm về chỉ số:
# remove, discard, add:
mySet.add(4)
print(mySet)  # mindset
mySet.add(1)
print(mySet)
# remove, discard: đều để xóa:
# remove:
# mySet.remove(9)  # xóa phần tử ko có trong set sẽ báo lỗi chương trình:
mySet.discard(9)  # xóa phần tử ko có bằng discard không gây ra lỗi
# đa phần mình sẽ dùng discard để xóa phần tử:
mySet.pop()  # xóa phần  tử ngẫu nhiên:
mySet.clear()  # xóa tất cả phần tử trong set: set()
print(mySet)

# Dictionary -> Hashmap -> Map:
print("Hello")

"""

# Tuple: list: khi muốn lưu trữ 1 list không bao giờ thay đổi thứ tự:
# const PI = 3.14
# ()
t1 = ("Faker", "Keria")  # []
t2 = (1,)  # Tuple nếu có 1 phần tử, đằng sau phải có ","
print(t2)
t = (1, 2, 3, 4, 5)
print(t[0])
print(t[len(t) - 1])
print(t[-1])
# t[0] = 9  TypeError: 'tuple' object does not support item assignment
t3 = (5, 2, 3) * 2  # 5 2 3 5 2 3
t4 = (5, 5, 6)  # 5 5 6
print(t3)
print(t3 + t4)  # (1, 2, 3, 4, 5, 6)
print(t3 < t4)  # True/ False:

# count:
print(t3.count(2))  ## count = 0 -> count+=1
# index: -> postion:
print(t3.index(3))  # Trả về vị trí phần tử đầu tiên thỏa mãn (số 3 mang index là 2)
print(t3.index(9))  # báo lỗi chương trình, k chạy được:
# pos = -1 -> dùng for i in range -> if : pos = i

# dict:
