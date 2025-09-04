import math
x= float(input("Nhập số tiền ban đầu: "))
lai_thang= 0.006
ky_han= 6
so_ky= 18 // 6
# Tính tiền sau 18 tháng
for i in range(so_ky):
    x *= (1 + lai_thang) ** ky_han
print("Tiền sau 18 tháng là: ", x)