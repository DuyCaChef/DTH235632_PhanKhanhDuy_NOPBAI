t=int(input("Nhập số giây: "))
hour= (t//3600)%24
minute= (t%3600)//60
second= t%60
print("Thời gian hiện tại là: ", hour,":",minute,":",second )