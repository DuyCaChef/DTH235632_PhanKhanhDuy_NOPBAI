import random

# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

# Tạo list gồm N số ngẫu nhiên không trùng nhau trong khoảng 0–100
lst = random.sample(range(0, 100), N)

print("List ngẫu nhiên không trùng nhau là:", lst)
