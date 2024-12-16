#In ra 10 so chia het cho 3 va 5 va la so duong
# n = 1
# count=0
# while True:
#     if n % 3 == 0 and n % 5 == 0:
#         count += 1
#         print(n)
#         if count == 10:
#             break
#     n += 1

# Kiểm tra 1 số có phải số nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó)
"""
Input: 13
Output: 13 là số nguyên tố

Input: 8
Output: 8 không phải số nguyên tố
Vì 8 chia hết cho 2 4

Bài tập tiếp: Tính tổng 10 số nguyên tố đầu tiên và hiển tḥ ra các số nguyên tố đó:
"""
"""def CheckPrime(n):
    count=0

    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        #print(f"{n} la so nguyen to")
        return True
    else:
        #print(f"{n} khong la so nguyen to")
        return False

n=int(input("Nhap so:"))
CheckPrime(n)

#Bài tập tiếp: Tính tổng 10 số nguyên tố đầu tiên và hiển tḥ ra các số nguyên tố đó:
count=0
n=1
sum=0
while count<10:
    if CheckPrime(n):
        count+=1
        sum = sum+n
        print(n)
    n+=1
print("Sum =",sum)"""
## Nhập vào 1 số và in ra số đảo ngược
## Input: 8539
## Output: 9358 ( %10, //10 và vòng lặp while)
"""n=int(input("Nhập số:"))
m=0 #sodaonguoc
while n>0:
    last_digit=n%10
    m=m*10+last_digit
    n=n//10
print(m)"""

## Nhập vào 1 số và tính tổng các chữ số của nó: 8539
## Output: 8 + 5 + 3 + 9 =...
"""n=int(input("Nhập số:"))
m=0
while n>0:
    last_digit=n%10
    m=m+last_digit
    n=n//10
print(m)"""

## Nhập vào 1 số và đếm số lượng các chữ số chẵn của nó: 853922
## Output: 3 ( 8 - 2 - 2 )
"""n=int(input("Nhập số:"))
count=0
while n>0:
    last_digit=n%10
    if last_digit %2 ==0:
        count+=1
    n=n//10
print(count)"""

# Cho a = 3, b = 4 ->
# Dùng phép biến đổi để swap 2 giá trị được là a = 4 và b = 3
#a=3
#b=4
#a,b=b,a

#print (a,b)
# Nhập số giây và in ra số giờ , phút , giây
## Input: 3905s
## Output: 1 giờ 5 phút 5 giây ( % // - 60)
sec=int(input("Nhập số giây: "))

days=sec//(24*60*60)
sec = sec %(24*60*60)
hours=sec//(60*60)
sec=sec%(60*60)
minutes=sec//60
sec=sec%(60)
print(f"{days} ngày {hours} giờ {minutes} phút {sec} giây")