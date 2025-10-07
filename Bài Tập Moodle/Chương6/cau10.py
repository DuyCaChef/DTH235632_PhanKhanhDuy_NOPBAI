# --- Hàm nhập ma trận ---
def nhap_ma_tran(ten):
    hang = int(input(f"Nhập số hàng của ma trận {ten}: "))
    cot = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    
    matrix = []
    for i in range(hang):
        row = list(map(float, input(f"  Hàng {i+1}: ").split()))
        while len(row) != cot:
            print(f" Số phần tử không khớp, cần {cot} phần tử!")
            row = list(map(float, input(f"  Hàng {i+1}: ").split()))
        matrix.append(row)
    return matrix

# --- Hàm in ma trận ---
def in_ma_tran(M):
    for row in M:
        print(" ".join(f"{x:6.2f}" for x in row))

# --- Hàm cộng 2 ma trận ---
def cong_ma_tran(A, B):
    hang = len(A)
    cot = len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(cot)] for i in range(hang)]
    return C

# --- Hàm hoán vị ma trận (Transpose) ---
def hoan_vi_ma_tran(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


# --- Chương trình chính ---
print("=== Nhập ma trận A ===")
A = nhap_ma_tran("A")

print("\n=== Nhập ma trận B ===")
B = nhap_ma_tran("B")

# --- Kiểm tra kích thước hợp lệ để cộng ---
if len(A) == len(B) and len(A[0]) == len(B[0]):
    print("\n➕ Tổng 2 ma trận A + B là:")
    tong = cong_ma_tran(A, B)
    in_ma_tran(tong)
else:
    print("\n Không thể cộng 2 ma trận có kích thước khác nhau!")

# --- Hoán vị ma trận ---
print("\n🔁 Ma trận hoán vị của A là:")
in_ma_tran(hoan_vi_ma_tran(A))

print("\n🔁 Ma trận hoán vị của B là:")
in_ma_tran(hoan_vi_ma_tran(B))
