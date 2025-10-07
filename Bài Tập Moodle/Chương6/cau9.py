import math

# --- Hàm kiểm tra số nguyên tố ---
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- Nhập mảng từ người dùng ---
chuoi = input("Nhập các số tự nhiên (cách nhau bằng dấu phẩy hoặc khoảng trắng): ")

# Xử lý chuỗi nhập vào (cho phép nhập: "3, 6, 7, 8" hoặc "3 6 7 8")
chuoi = chuoi.replace(',', ' ')
M = [int(x) for x in chuoi.split() if x.isdigit()]

# --- Tách các loại số ---
so_le = [x for x in M if x % 2 != 0]
so_chan = [x for x in M if x % 2 == 0]
so_ngto = [x for x in M if la_so_nguyen_to(x)]
so_khong_ngto = [x for x in M if not la_so_nguyen_to(x)]

# --- uất kết quả ---
print("\nMảng đã nhập:", M)
print(so_le, "→ Có", len(so_le), "số lẻ.")
print(so_chan, "→ Có", len(so_chan), "số chẵn.")
print(so_ngto, "→ Có", len(so_ngto), "số nguyên tố.")
print(so_khong_ngto, "→ Có", len(so_khong_ngto), "số không phải nguyên tố.")
