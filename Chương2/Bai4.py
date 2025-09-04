month= int(input("Nhập tháng (1-12): "))
# sử dụng match-case để xác định số ngày trong tháng(tương tự switch-case trong C/C++)
match month: 
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Tháng", month, "có 31 ngày")
    case 4 | 6 | 9 | 11:
        print("Tháng", month, "có 30 ngày")
    case 2:
        # Kiểm tra năm nhận
        year= int(input("Nhập năm: "))
        if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("Tháng", month, "có 29 ngày")
        else:
            print("Tháng", month, "có 28 ngày")
    case _:
        print("Tháng không hợp lệ")