n= int(input("Nhập một số từ 0 - 99: "))
if n < 0 or n > 99:
    print("Số không hợp lệ")
else:
    hang_chuc= n // 10
    hang_don_vi= n % 10
    # từ điển đọc số 0-99
    doc_so= ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín",]
    # xử lý cách đọc
    if n < 10:
        ket_qua= doc_so[n]
    else:
        # đọc hàng chục
        if hang_chuc == 1:
            ket_qua= "mười"
        else:
            chuoi = doc_so[hang_chuc] + " mươi"

        # đọc hàng đơn vị
        if hang_don_vi == 0:
            ket_qua= chuoi
        elif hang_don_vi == 1:
            ket_qua= chuoi + " mốt"
        elif hang_don_vi == 5:
            ket_qua= chuoi + " lăm"
        else:
            ket_qua= chuoi + " " + doc_so[hang_don_vi]
    print("Cách đọc:", ket_qua)