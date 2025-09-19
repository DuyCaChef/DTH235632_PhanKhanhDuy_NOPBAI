from math import sqrt

xA= int(input("Nhập xA: "))
xB= int(input("Nhập xB: "))
yA= int(input("Nhập yA: "))
yB= int(input("Nhập yB: "))

distance = sqrt((xB- xA)**2 + (yB-yA)**2)

print("Độ dài cạnh: ", distance)