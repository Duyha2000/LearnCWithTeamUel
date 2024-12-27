# 1
"""s = input("Nhập chuỗi: ")
c = input("Nhập kí tự: ")
count = 0
for i in s:
    if i == c:
        count += 1
print(count)
print(s.count(c))"""
# 2
"""s = input("Nhap chuoi: ")
c = input("Nhap ki tu: ")
pos = -1
for i in range(len(s)):
    if s[i] == c:
        pos = i
        break
print(pos)"""

# 4.Palindrome
# abcddcba là chuỗi palindrome vì đảo trước sau đều giống nhau
"""s = input("Nhap chuoi:")
if s[::-1] == s:
    print("YES")
else:
    print("NO")"""

# 5. pseudo-palindrome
# abcdxxacba với n = 3 là chuỗi giả palindrome vì abc - cba ( 3 ký tự)
#        -1
"""s = input("Nhap chuoi:")
n = int(input("Nhap so ki tu muon kiem tra:"))

if s[:n:1] == s[:-n - 1:-1]:
    print("YES")
else:
    print("NO")"""

# Set.1. Loại bỏ phần tử trùng lặp và in kết quả
"""list = []
for i in range(5):
    list.append(int(input("Nhap 5 so:")))  # 1 1 1 2 3
print(set(list))
print(len(set(list)))"""

# 2.lưu lại các từ (word) mà người dùng nhập vào
"""vocab = set()

while True:
    word = input("Nhap vocab").strip()  # stop
    if word != "STOP":
        vocab.add(word)
    if word == "STOP":
        break

# Xóa phần tử STOP:
vocab.discard("STOP")  # remove:
print(vocab)
print(len(vocab))"""

# 3. Xóa phần tử khỏi Set
my_set = {'a', 'b', 'c', 'd', 'e'}
x = input("Nhap tu muon kiem tra: ")
if x in my_set:
    my_set.remove(x)
else:
    print(f"{x} khong ton tai")
print(my_set.pop())
print(my_set)
