from math import sqrt
print("Chương trình giải phương trình bậc hai: ")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print(f"Phương trình có một nghiệm: x = {x}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x1 = x2 = {x}")
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")