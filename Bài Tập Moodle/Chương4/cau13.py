def tong_uoc_so(n):
    """Trả về tổng các ước số dương của n (không tính n)."""
    tong = 1  # 1 luôn là ước số (n > 1)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:  # tránh cộng trùng khi n là số chính phương
                tong += n // i
    return tong if n > 1 else 0


def la_so_hoan_thien(n):
    """Kiểm tra số hoàn thiện."""
    return tong_uoc_so(n) == n


def la_so_thinh_vuong(n):
    """Kiểm tra số thịnh vượng."""
    return tong_uoc_so(n) > n


# --- Chạy thử ---
n = int(input("Nhập n: "))

if la_so_hoan_thien(n):
    print(n, "là số hoàn thiện.")
elif la_so_thinh_vuong(n):
    print(n, "là số thịnh vượng.")
else:
    print(n, "không phải số hoàn thiện, cũng không phải số thịnh vượng.")
