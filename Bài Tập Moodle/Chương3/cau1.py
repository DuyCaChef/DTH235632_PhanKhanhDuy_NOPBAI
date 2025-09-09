print("Chương trình kiểm tra năm nhuần")
year = int(input("Nhập vào một năm: "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print(f"{year} là năm nhuần")
else: 
    print(f"{year} không phải là năm nhuần")
