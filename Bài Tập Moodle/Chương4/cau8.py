import math

x= float(input("Nhập x (x>0): "))
a= float(input("Nhập a (a>0, a#1): "))
if x>0 and a>0 and a!=1:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x}")
else:
    print("Điều kiện không hợp lệ !")
 