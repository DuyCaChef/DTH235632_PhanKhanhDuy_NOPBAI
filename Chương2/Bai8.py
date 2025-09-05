n= int(input("Nhập số nguyên n(1-9): "))
if n < 1 or n > 9:
    print("Số nhập vào không hợp lệ")
else:
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
