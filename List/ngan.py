'''#bai 1
list1=[1,2,3,4,5]
sum1=0
for i in range (len(list1)):
    sum1+= list1[i]
"""
for i in list1:
    sum += i
"""
print(sum1)

#bai2: count, sum -> >0 (số hạng dương)
list2=[-2,-2,2,3,4,7,-10]
count=0
sum2=0
for i in list2:
    if i>0:
        sum2+=i
        count+=1
print(f"có {count} số dương và tổng là {sum2} ")'''

'''#bai 3
list=[-1,6,4,7,3,10,-19]
sum1=0
sum2=0
count=0
for i in list:
    sum1+=i
    if i>0:
        sum2+=i
        count+=1
aver1=sum1 / (len(list)-1)
aver2=sum2 / count
print(aver1)
print(aver2)
'''

'''#bai 4: 3 (số 10)
list=[0,9,6,-10,-2,4,5]
pos=-1
for i in range (len(list)):
    if list[i] <0:
        pos=i
        break
print(pos)
'''

#bai 5: [1,3,-2,-4,5,-9,-8]
# Output: vị trí 4 ( số 5)

list=[1,3,-2,-4,5,-9,-8]
pos=-1
for i in range (len(list)):
    if list[i]>0:
        pos=i
print(pos)


