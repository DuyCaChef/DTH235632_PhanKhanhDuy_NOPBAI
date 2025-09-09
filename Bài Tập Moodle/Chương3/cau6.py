print("Chương trình đọc số:")

# Function to convert number to Vietnamese text
def number_to_text(n):
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return units[n]
    elif n < 100:
        ten = n // 10
        unit = n % 10
        if unit == 0:
            return tens[ten]
        else:
            return f"{tens[ten]} {units[unit]}"
    else:
        return "Số không hợp lệ"

# Input number
n = int(input("Nhập số n (tối đa 2 chữ số): "))
if 0 <= n < 100:
    print("Cách đọc:", number_to_text(n))
else:
    print("Vui lòng nhập số từ 0 đến 99.")