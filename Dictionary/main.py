# Dictionary: từ điển -hashmap - map

# 1 menu gồm có tên món ăn + giá tiền, làm thế nào để lưu giá trị:

# Pho - 20000
# Bun bo - 30000
# Chao long - 15000

# khởi tạo ra 2 list:
names = ["Pho", "Bun bo", "chao long"]
prices = [20000, 30000, 15000]  # 15000 -  20000 - 30000
"""
for i in range(len(names)):
    print(names[i], prices[i])
"""

# Dictionary: key - value:
menu = {
    "Pho": 20000,  # Key: value
    "Bun bo": 30000,
    "Chao long": 15000,
}

# Truy cập và hiển thị menu:
# menu.items(): ứng với tất cả giá trị key - value của dictionary

# Thêm 1 món bánh tráng:
# menu["key"] = value: thêm mới cặp key value nếu key đó chưa tồn tại trong dictionary
# menu["key"] = value: cập nhật lại value nếu key đó đã tồn tại
menu["banh trang"] = 30000
menu["Pho"] = 10000
# Xóa món: bằng hàm pop("key")
menu.pop("Bun bo")

# Truy cập vào Phở xem giá bao nhiêu tiền:
print(menu.get("Bun dau"))  # 10000, trả về giá trị None nếu không tìm thấy
# print(menu["Bun dau"])  # 10000, nếu truy cập 1 key không có trong Dictionary thì sẽ báo lỗi

# menu.items(): "Pho": 20000 -   "Bun bo": 30000 - "Chao long": 15000

# key , value
for k, p in menu.items():
    print(f"{k} : {p}")

# Duyệt qua tất cả các value trong dictionary:
for price in menu.values():
    print(f"{price}")  # 10000 - 15000 - 30000

# Duyệt qua tất cả các key trong dictionary:
for name in menu:
    print(f"{name}")

"""
Bài 1: Đếm số lần xuất hiện của các phần tử
Đề bài: Đếm số lần xuất hiện của mỗi phần tử trong một danh sách.
lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
Kết quả:
{'apple': 3, 'banana': 2, 'orange': 1}
"""
lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_dict = {}
# Bài toán thống kê: dictionary:
# Nếu món ăn chưa xuất hiện trong dictionary, tạo ra 1 cặp key - value = 1
"""
count = {
    "apple": 2,
    "banana": 1,
    # "apple": 1, # Nếu key đã xuất hiện trong dictionary rồi, tăng value lên 1
}
"""
for item in lst:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

for k, v in count_dict.items():
    print(k, v)
