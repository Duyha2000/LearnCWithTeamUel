"""lst=[1,3,5,7,9]
sum=0
for i in lst:
    sum +=i
print(sum)"""


"""lst2=[1,3,5,7,9,2,4,6]
count=0
sum=0
for i in lst2:
    count+=1
    sum+=i
print(f"Tổng là {sum} và số lượng là {count} số hạng ")"""


numbers = input("Nhập các số hạng, cách nhau bằng dấu cách: ")
numbers = list(map(int, numbers.split()))
positive_count = 0
positive_sum = 0
for num in numbers:
    if num > 0:
        positive_count += 1
        positive_sum += num
print("Số lượng các số hạng dương:", positive_count)
print("Tổng các số hạng dương:", positive_sum)

