a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

operator = input("Nhập phép toán (+, -, *, /): ")

if operator == '+':
    print(f"Kết quả: {a} + {b} = {a + b}")
elif operator == '-':
    print(f"Kết quả: {a} - {b} = {a - b}")
elif operator == '*':
    print(f"Kết quả: {a} * {b} = {a * b}")
elif operator == '/':
    if b != 0:
        print(f"Kết quả: {a} / {b} = {a / b}")
    else:
        print("Lỗi: Không thể chia cho 0.")
else:
    print("Phép toán không hợp lệ.")
