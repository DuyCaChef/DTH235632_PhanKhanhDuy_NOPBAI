n= int(input("Nhập số nguyên n: "))
s1=0
for i in range(1, n+1):
    s1 += i
print(f"Tổng từ 1 đến {n} là: {s1}")
s2= n * n
print("Tổng của bình phương từ 1 đến", n, "là:", s2)
s3 = 0
for i in range (1, n+1):
    s3 += 2 * i
print("Tổng của cấp số cộng 2, 4, 6,... đến", 2*n, "là:", s3)
s4 = 0
for i in range (1, n+1):
    s4 += i ** 2
print("Tổng của bình phương từ 1 đến", n, "là:", s4)
s5 = 0
for i in range (1, n+1):
    s5 += 1 / i
print("Tổng của dãy 1 + 1/2 + 1/3 + ... + 1/n là:", s5)