import math

def giai_pt_bac2(a, b, c):
    # Kiểm tra các hệ số
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            return f"Phương trình có một nghiệm: {-c/b}"
    
    # Tính delta
    delta = b*b - 4*a*c
    
    # Kiểm tra và tính nghiệm theo delta
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return f"Phương trình có 2 nghiệm phân biệt:\nx1 = {x1}\nx2 = {x2}"
    elif delta == 0:
        x = -b/(2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm trong tập số thực"

# Nhập các hệ số từ người dùng
print("Nhập các hệ số của phương trình ax² + bx + c = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Giải và in kết quả
ket_qua = giai_pt_bac2(a, b, c)
print("\nKết quả:")
print(ket_qua)
