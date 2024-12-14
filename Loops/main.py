# In ra 10 số chia hết cho 3,5 và là số dương.
# Output: 15 30 45 ... 105 120
## -> tăng dần, kiểm tra điều kiện đến khi nào đủ 10 số thỏa mãn thì dừng vòng lặp:
## count = 0 -> count += 1 mỗi khi 1 số thỏa mãn:
"""
n = 8
count = 0
for i in range(1, n + 1): # 1 -> 13
    if n % i == 0:
        count += 1

if count == 2:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")
"""

""""
n = 2
count_prime = 0

while count_prime < 10:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n, "là số nguyên tố")
        count_prime += 1

    n += 1
"""

"""t = int(input("Nhập số giây:"))
hour = (t // 3600) % 24
minute = (t % 3600) // 60
second = (t % 3600) % 60
print(hour, "giờ", minute, "phút", second, "giây")"""