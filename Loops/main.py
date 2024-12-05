"""
Vòng lặp: miêu tả những hành động lặpdđi lặp lại
Ví dụ: hàng ngày đi học từ 8h sáng -> 12h trưa -> đi ăn ăn -> đánh cầu lông -> ăn tối
In ra chữ xin chào 5 lần, nếu không dùng vòng lặp
For
While

1. Vòng lặp for in range(phạm vi gì đấy):
for i in range (start, end, step)

start: giá trị bắt  đầu vòng lặp, nếu không có start thì sẽ lấy số 0
end: giá trị cuối cùng của vòng lặp (không bao gồm giá trị này)
step: bước nhảy, nếu không viết gì thì step là 1
In ra các số từ 0 đến 4:
print(0)
print(1)
print(2)
print(3)
print(4)

for(int i = 0 ; i<=5;i++){print(i}
for i in range(5):
    print(i, end =" ")
In ra các số chẵn từ 9 về 0:
10 -> 9 ... 8 7
for i in range (9,-1,-1):
    if i%2==0:
        print(i, end=" ")

Exercise 2: Numbers Divisible by 3 and 5
Task: Write a program that takes two integers a and b and displays all numbers between them divisible by both 3 and 5.

Input: a,b -> a = 1 , b = 50
Output: các số chia hết cho cả 3 và 5 trong đoạn a , b
15 30 45
for i in range (a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
Start -> end
in range(start,end)
a = int(input("Nhập a: ")) # a = 1
b = int(input("Nhập b: ")) # b = 50
# 1 -> 50
while a < b:
    if a % 3 == 0 and a % 5 == 0:
        print(a, end=" ")
    # step:
    a += 1

Exercise 13: Validate User Input
Write a program in Python that uses a while loop to validate user input for entering a valid age. The program should ensure that the age entered is between 0 and 120 (inclusive). If the user enters an invalid value, the program should display an error message and prompt the user to re-enter the age.

Input: tuổi
Nếu nhập tuổi < 0 hoặc tuổi > 150 thì sẽ in ra lỗi, tuổi không hợp lệ
Cứ nhập lỗi, hiển thị thông báo nhập lại
While: lặp khi nào:

Username: không được để trống
Password: không được để trống
"""

# break
# while True:
#     age = int(input("Nhập tuổi của bạn: "))
#     if 0 < age <= 150:
#         print ("Valid age")
#         break
#     else:
#         print("Invalid")
# break: làm vỡ, phá vỡ
# break giúp thoát vòng lặp
# In ra số đầu tiên chia hết cho 3 và 5 trong khoảng từ 1 đến 50:
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end=" ")
#         break
# Continue: 1 2 - 4 5 6 7 8 9
# Continue: bỏ qua
# for i in range(1,10):
#     if i == 3:
#         continue
#     print(i, end=" ")

# for i in range(1,10):
#     if i != 3:
#         print(i, end=" ")
# In ra các số chẵn từ 1 đến 10    1 2 3 4 5 6 ... 10
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i, end=" ")
# While True -> break: tránh vòng lặp vô hạn =))
"""
Exercise 14: Guess the Number Game
Write a program to simulate a number guessing game:
The program randomly selects a number between 1 and 100.
The user repeatedly enters guesses.
Use a while loop to keep asking for input until the user guesses the correct number.
The program should provide hints like "Too high!" or "Too low!" after each guess.
Extension: Count the number of guesses and display it when the user wins.

Input: X 
Mỗi lần đoán, nếu giá trị nhỏ hơn X thì sẽ in ra Too low
nếu lớn hơn thì sẽ in ra Too high
"""
## while: nếu condition là True thì sẽ chạy code trong while, còn condition là false thoát vòng lặp, break
# X = int(input("Số của chương trình là")) # 30
#
# ## break, chuyển giá trị condition thành false
# # Khởi tạo boolean isCheck
# isCheck = True
# while isCheck:
#     number = int(input("Mời bạn đoán số:"))
#     if number < X:
#         print("Too low!")
#     elif number > X:
#         print("Too high!")
#     else:
#         print("Correct!")
#         isCheck = False
# # Vòng lặp vô hạn
# # Làm menu chức năng: OOP:
#
# # In ra số dương nhỏ nhất chia hết cho 3 5 và 7:
# ## n = 1 -> 2 , 3 , 4 , 5 , 6 ,7 ,8 ,9 ... -> đầu tiên thỏa mãn chia hết cho 3,5,7
# n = 1
# isCheck = True
# while isCheck:
#     if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
#         print(n, end=" ") # 105
#         isCheck = False
#     # step:
#     n += 1
## Vòng lặp (for i in range, while) -> for else while else, continue, [list, function]
## Javascript:
## Java:

"""
Exercise 10: Shape Calculator
Task: Develop a program to calculate the perimeter and area of shapes based on a menu of options.
Menu:
1. Calculate the perimeter and area of a rectangle.
2. Calculate the perimeter and area of a triangle.
3. Calculate the perimeter and area of a circle.
4. Exit. 
"""

while True:
    print("Menu:")
    print("1. Calculate the perimeter and area of a rectangle")
    print("2. Calculate the perimeter and area of a triangle")
    print("3. Calculate the perimeter and area of a circle")
    print("4. Exit.")
    print("Mời bạn chọn món:")
    choice = int(input("Choice:")) # switch- match: thay đổi , case: trường hợp
    #     # if choice == 1:
    #     #     print("The perimeter and area of a rectangle")
    #     # elif choice == 2:
    #     #     print("The perimeter and area of a triangle")
    #     # elif choice == 3:
    #     #     print("The perimeter and area of a circle")
    #     # elif choice == 4:
    #     #     print("Goodbye!")
    #     #     break
    #     # else:
    #     #     print("Invalid choice!")
    # String, list, function (recursion)

    match choice:
        case 1:
            print("The perimeter and area of a rectangle")
        case 2:
            print("The perimeter and area of a triangle")
        case 3:
            print("The perimeter and area of a circle")
        case 4:
            print("Goodbye!")
            break
        case _:  ## khi chọn không phải 1 2 3 4 thì sẽ chạy vào case này, default
            print("That's not a valid choice.")
## 2 vòng for vẽ hình ngôi sao

