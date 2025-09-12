from random import randrange
while True: 
    somay = randrange(1,101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Mời bạn đoán số (1-100): "))
        print("Bạn đoán lần thứ ", solandoan,":")
        if somay == songuoi:
            print("Chúc mừng bạn đã đoán trúng số: ", somay)
            win = True
            break
        if somay > songuoi: 
            print("Bạn đã đoán sai! Số bạn đoán nhỏ hơn số máy")
        elif somay < songuoi:
            print("Bạn đã đoán sai! số bạn đoá lớn hơn số máy")
    if win == False:
        print("GAME OVER !!!, số máy là: ", somay)
    hoi =input("Tiếp không ?")
    if hoi == "k": 
        break
print("Cám ơn bạn đã chơi game!")
