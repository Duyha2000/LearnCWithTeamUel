# 1 Bài tập 1: Đếm số lần xuất hiện của ký tự c trong chuỗi s
# Đề bài
# Cho xâu (chuỗi) s và một ký tự c được nhập từ bàn phím.
# Yêu cầu: In ra số lần xuất hiện của ký tự c trong xâu s.
'''s = input("nhap chuoi s: ")
c = input("nhap ki tu: ")
count = 0
for i in s:
    if i == c:
        count += 1
print(count)'''

'''Bài tập 2: Tìm vị trí đầu tiên của ký tự c trong chuỗi s
Đề bài
Cho xâu s và ký tự c được nhập từ bàn phím.
Yêu cầu: In ra vị trí đầu tiên (chỉ số index) mà ký tự c xuất hiện trong s. Nếu ký tự c không tồn tại, in -1.
'''

'''s = input("nhap chuoi s: ")
c = input("nhap ki tu: ")
pos = -1
for i in range(len(s)):
    if s[i] == c:
        pos = i
        break
print(pos)
'''
# Bài tập 4: Kiểm tra chuỗi có phải là palindrome hay không
'''Đề bài
Cho một xâu s. Kiểm tra xem khi đảo ngược xâu s (reverse), ta có thu được chính s hay không.
Nếu có, in ra màn hình "YES", ngược lại in "NO".'''
'''s = input("nhap chuoi: ")
if s[::-1] == s:
    print("yes")
else:
    print("no")'''

'''1. Bài tập 1 set :Loại bỏ phần tử trùng lặp và in kết quả
Đề bài:
Bạn được nhập một danh sách các số nguyên từ bàn phím (có thể trùng lặp).'''
'''list1 = []
for i in range(7):
    list1.append(input("nhap so: "))
set1 = set(list1)
print(set1)
print(len(set1))'''

'''2. Bài tập 2: Quản lý từ vựng (bộ từ vựng duy nhất)
Đề bài
Bạn muốn lưu lại các từ (word) mà người dùng nhập vào (có thể trùng lặp).
Yêu cầu:
Tạo một Set rỗng ban đầu, gọi là vocab.
Người dùng được nhập nhiều từ (theo từng dòng hoặc theo chuỗi).
Mỗi khi nhập 1 từ, hãy thêm từ đó vào vocab.
Khi người dùng nhập từ "STOP" thì dừng lại.
In ra tất cả các từ duy nhất đã nhập, kèm số lượng.'''

'''# vocab là set() -> cho nó nhập freestyle thì dùng vòng lặp for hay while nhỉ
# while ha anh
vocab = set()
while True:
    x = input("nhap vao set: ")
    vocab.add(x)
    # set có sẵn rồi không cần count đâu em
    if x == "sto p":
        break
# Xóa phần tử STOP bằng discard:
vocab.discard("stop")
print(vocab)
print(len(vocab))
'''

'''Bài tập 3: Xóa phần tử khỏi Set
Đề bài
Cho sẵn (hoặc nhập vào) một Set các ký tự, ví dụ { 'a', 'b', 'c', 'd', 'e' }.
Yêu cầu:
Nhập từ bàn phím một ký tự x.
Nếu ký tự x có trong Set, hãy dùng phương thức remove(x) để xóa nó và in ra Set sau khi xóa.
Nếu x không có trong Set, in ra thông báo 'Phần tử không tồn tại trong Set'.
Sau đó, sử dụng pop() để xóa ngẫu nhiên một phần tử khỏi Set (nếu còn phần tử) và in ra phần tử vừa bị xóa, kèm trạng thái Set mới.
'''

set3 = {2, 3, 4, 5, 6, "hi", "hello"}
x = input("nhap mot so hoac ki tu bat ki: ")  # string: "hello"

"""
if x in set3:
    if x.isdigit():  # digit():
        set3.discard(int(x))
    set3.discard(x)
else:
    set3.pop()
print(set3)
"""
for i in set3:
    if x.isdigit() and int(x) == i:
        set3.discard(i)
        break
    if x == i:
        set3.discard(i)
        break
print(set3)
"""
txt = "50800"

x = txt.isdigit()

isDigit, isalpha, ... 
print(x)
"""
