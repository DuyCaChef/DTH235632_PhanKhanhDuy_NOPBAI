import re

def NegativeNumberInStrings(s):
    # Tìm tất cả số nguyên âm (dấu '-' + 1 hoặc nhiều chữ số)
    numbers = re.findall(r'-\d+', s)
    # Chuyển thành số nguyên
    return [int(num) for num in numbers]


# --- Chạy thử ---
s = "abc-5xyz-12k9l--p"
result = NegativeNumberInStrings(s)
print("Các số nguyên âm trong chuỗi:", result)
