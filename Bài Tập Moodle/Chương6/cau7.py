# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

lst = []
for i in range(N):
    while True:
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        # Nếu là phần tử đầu tiên hoặc lớn hơn phần tử trước đó thì hợp lệ
        if i == 0 or x > lst[-1]:
            lst.append(x)
            break
        else:
            print("Phải nhập số lớn hơn số trước đó! Nhập lại...")

print("\n✅ Dãy số tăng dần bạn vừa nhập là:")
print(lst)
