'''n=1
count=0
while True:
    if n%3==0 and n%5==0:
        print(n)
        count+=1
    if count==10:
        break
    n+=1'''

# Kiểm tra 1 số có phải số nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó)
"""
Input: 13
Output: 13 là số nguyên tố

Input: 8
Output: 8 không phải số nguyên tố
Vì 8 chia hết cho 2 4

13: [ 2 - 12] -> Ko chia hết số nào đoạn này, nó mới là nguyên tố
8: [2,7] -> Chia hết cho 2 4 
"""
'''n=int(input("nhập n: ")) # 8
# isCheck = true (kiểm tra có thỏa mãn hay không)
isCheck = True
for i in range (2,int(n**0.5)+1):
    if n%i==0:
        isCheck = False ## isCheck = false
if isCheck :
    print (f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")'''
#Bài tập tiếp: Tính tổng 10 số nguyên tố đầu tiên và hiển tḥ ra các số nguyên tố đó:
sum=0
count = 0
n = 2 ## 2 -> . . . . . . .
# Def:
# Function nhớ return nhé em
def songuyento(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
           return False ## isCheck = false
    return True

while count <10:
    if songuyento(n):
        sum+=n
        count+=1
        print(n)
    # Step:
    n += 1

print(sum)

