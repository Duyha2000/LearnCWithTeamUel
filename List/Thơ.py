#1. Tính tổng các phần tử của danh sách
"""list=[]
sum=0
# For để input:
for i in range(5):
    list.append(int(input()))

# For tính toán logic:
for i in range (len(list)):
    sum+=list[i]
For each:
for i in list1:
    sum += i

print(sum)"""

#2.Đếm số dương và tổng các số dương
"""list=[]
list_p=[]
count=0
count_p=0
sum=0
sum_p=0
for i in range (5):
    list.append(int(input("Nhap so:")))
print(list)
# i đại diện từng số trong lst [1,3,5,7,9]
# 1 3 5 7 9
for i in list:
    sum+=i
tb=sum/len(list)
print("Trung bình cộng của cả danh sách=", tb)

for i in list:
    if i>0:
        list_p.append(i)

for i in list_p:
    sum_p+=i
tb_p=sum_p/len(list_p)
print("Trung bình cộng của các số dương=", tb_p)
#print("Số lượng",count)
#print("Tổng",sum)"""
#3. Tính trung bình của list và của các số dương trong list

#4.Tìm "vị trí" phần tử âm đầu tiên trong list
"""list=[]
for i in range (5):
    list.append(int(input("Nhap so:")))
print(list)
#for i in list:
# 3 -7 8 10 2
pos = -1
for i in range (len(list)):
    if list[i]<0:
        pos=i
        break
print(pos)"""

#5.Tìm vị trí số dương cuối cùng
list=[]
for i in range (5):
    list.append(int(input("Nhap so:")))
print(list)

pos = -1
for i in range (len(list)):
    if list[i]>0:
        pos=i
print(pos)
