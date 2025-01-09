"""
Bài tập 1: Tạo một dictionary với khóa kiểu int và giá trị kiểu string.
Thêm ít nhất 5 cặp khóa - giá trị vào dictionary.
In ra giá trị của một khóa bất kỳ. In ra kích thước của dictionary.

Input: Tran Duc Duy Tran Duc
Output: 1 - Tran
        2 - Duc
        3 - Duy
        4 - Tran
        5 - Duc 5
"""
menu = {
    1: "toan",
    2: "ly",
    3: "hoa",
    4: "sinh",
    5: "anh"
}

for key, value in menu.items():
    print(f"{key} - {value}")

print("Kich thuoc cua dict la: ", len(menu))
