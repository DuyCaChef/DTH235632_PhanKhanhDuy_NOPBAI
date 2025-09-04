a= float(input("Nhập số a: "))
b= float(input("Nhập số b: "))
ch= input("Nhập phép tính (+, -, *, /): ")
if ch == '+':
    result = a + b
    print("Kết quả: ", result)
elif ch == '-':
    result = a - b
    print("Kết quả: ", result)
elif ch == '*':
    result = a * b
    print("Kết quả: ", result)
elif ch == '/':
    if b != 0:
        result = a / b
        print("Kết quả: ", result)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print(ch, " không phải là một toán tử!!!")