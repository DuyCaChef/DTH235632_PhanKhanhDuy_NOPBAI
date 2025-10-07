def xu_ly_chuoi(s):
    vowels = "aeiouAEIOU"   # nguyên âm (kể cả hoa và thường)

    dem_hoa = dem_thuong = dem_so = dem_khoang_trang = 0
    dem_dac_biet = dem_nguyen_am = dem_phu_am = 0

    for ch in s:
        if ch.isupper():   # chữ hoa
            dem_hoa += 1
        if ch.islower():   # chữ thường
            dem_thuong += 1
        if ch.isdigit():   # chữ số
            dem_so += 1
        if ch.isspace():   # khoảng trắng
            dem_khoang_trang += 1
        if not ch.isalnum() and not ch.isspace():  # ký tự đặc biệt
            dem_dac_biet += 1

        # kiểm tra nguyên âm / phụ âm
        if ch.isalpha():   # là chữ cái
            if ch in vowels:
                dem_nguyen_am += 1
            else:
                dem_phu_am += 1

    print("Số chữ IN HOA:", dem_hoa)
    print("Số chữ in thường:", dem_thuong)
    print("Số chữ số:", dem_so)
    print("Số ký tự đặc biệt:", dem_dac_biet)
    print("Số khoảng trắng:", dem_khoang_trang)
    print("Số nguyên âm:", dem_nguyen_am)
    print("Số phụ âm:", dem_phu_am)


# --- Chạy chương trình ---
chuoi = input("Nhập chuỗi: ")
xu_ly_chuoi(chuoi)

