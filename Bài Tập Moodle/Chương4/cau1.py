from math import sqrt
print("Chương trình tính diện tích Tam Giác: ")
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
if (a <= 0 or b <= 0 or c <= 0) or (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Ba cạnh a, b, c không thể tạo thành tam giác!")
else:
    cv = a+b+c
    p = cv /2
    dt= sqrt(  p*(p-a)*(p-b)*(p-c)  )
print("Diện tích tam giác là: ", dt)
