from datetime import datetime, timedelta

# nhập ngày từ người dùng
date_input = input("Nhập ngày (dd/mm/yyyy): ")
try:
    # ngày được nhập
    current_date = datetime.strptime(date_input, "%d/%m/%Y")

    # tính ngày kế tiếp
    next_date = current_date + timedelta(days=1)

    # in kết qủa
    print("Ngày kế tiếp là:", next_date.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày không hợp lệ. Vui lòng nhập theo định dạng dd/mm/yyyy.")