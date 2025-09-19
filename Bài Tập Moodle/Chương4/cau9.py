from math import sqrt
n= int(input("Nhập số n: "))
s=0
for i in range(1,n):
    s= sqrt(2+s)
print(f"S({n}) = {s}")