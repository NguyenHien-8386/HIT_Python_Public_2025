luong = int(input("nhập lương: "))
if luong == 15000000:
    thue = luong*0.3
elif luong >= 7000000 and luong <= 15000000:
    thue = luong*0.2
elif luong < 7000000:
    thue = luong*0.1
else:
    print("lương lố quá rồi !")
x = int(thue)
y = int(luong-thue)
print("thuế: ", x, " thu nhập: ", y)
