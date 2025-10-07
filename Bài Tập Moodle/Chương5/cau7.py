def toi_uu_chuoi(s):
    # Xóa khoảng trắng dư thừa, tách thành list các từ
    words = s.strip().split()
    # Viết hoa chữ cái đầu mỗi từ, các chữ cái sau viết thường
    words = [w.capitalize() for w in words]
    # Ghép lại thành chuỗi mới
    return " ".join(words)


# --- Chạy thử ---
s = "  TRần   duY   thAnH   "
print("Input :", repr(s))
print("Output:", toi_uu_chuoi(s))
