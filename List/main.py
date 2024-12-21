# Slicing: Lấy ra 1 danh sách con trong python:
lst = [1,2,7,9,8]
# [2,7]

# lst[start_index : end_index : step]
# for i in range(a, b+1)
# [start, end): lấy đầu, bỏ đuôi
print(lst[0: 2 : 1]) # 0 --> 2
print(lst[1:4:1]) # [2,7,9]

lst2 = [0,2,2,3,4,2,6,7,8,9]
#                          ->
print(lst2[2:6:2]) # 2 - > 5 : 2 - 4 [2, 4]
print(lst2[0:9:3]) # 0 -> 8 -> lstcon = [0,3,6]

print(lst2[3::3]) # start: 3 , step :3 ( bỏ end):
# step > 0 -> các phần tử đi từ trái qua phải ->
# 3 ứng với số 3 ->
print(lst2[3:9:3]) # 3 - 8 -> [3,6]
print(lst2[3::3]) # [3, 6, 9]
"""
vidu_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        -->
                                      <--
print(vidu_list[:5:2]) # Bỏ trống chỉ số đầu, bước nhảy dương -> 0 2 4
print(vidu_list[:5:-2]) # Bỏ trống chỉ số đầu, bước nhảy âm -> 9 7 
print(vidu_list[5::2]) # Bỏ trống chỉ số cuối, bước nhảy dương -> 5 7 9
print(vidu_list[5::-2]) # Bỏ trống chỉ số cuối, bước nhảy âm -> 5 3 1
print(vidu_list[::2]) # Bỏ trống cả chỉ số đầu và cuối, bước nhảy dương -> 0 2 4 6 8
print(vidu_list[::-2]) # Bỏ trống cả chỉ số đầu và cuối, bước nhảy âm -> 1 3 5 7 9
print(vidu_list[::]) # Bỏ trống tất cả các chỉ số và bước nhảy -> 0 1 2 3 4 5 6 7 8 9 
print(vidu_list[:5]) # Bỏ trống chỉ số đầu và bước nhảy -> 0 1 2 3 4
print(vidu_list[5:]) # Bỏ trống chỉ số cuối và bước nhảy -> 5 6 7 8 9
"""
# contain() -> True/False (kiểm tra số có tồn tại trong list hay không)
# 1 list từ 0 đến 9
# Nhập vaào 1 số và kiểm tra số đó có nằm trong list hay không, có in ra True, k có in ra false
X = int(input())
"""
if lst2.contains__(X):
    print("Yes")
else:
    print("No")
"""
count = 0
for i in lst2:
    if i == X:
        count +=1

if count == 0:
    print("No")
else:
    print("Yesssssss")
# Matrix: [1,2,3,[1,2,3] , [1,2,3]]

# count, sum, max , min
print(max(lst2))
print(min(lst2))
print(lst2.count(2))
# Reverse list trong python:
# lst2.reverse()
print(lst2[: : -1])


