month = int(input("Nhập vào một tháng(1-12):"))
if month in[1,2,3,4]:
    print("Tháng",month , "thuộc quý 1")
elif month in[5,6,7,8]:
    print("Tháng",month , "thuộc quý 2")
elif month in[9,10,11,12]:
    print("Tháng",month , "thuộc quý 3")
else:
    print("Tháng không hợp lệ")