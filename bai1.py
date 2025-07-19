thang = int(input("nhập tháng: "))
nam = int(input("nhập năm: "))
nam_nhuan = False
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    nam_nhuan = True
if thang in [1, 3, 5, 7, 8, 12]:
    so_ngay = 31
elif thang in [4, 6, 8, 11]:
    so_ngay = 30
elif thang == 2:
    if nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28
print("tháng ", thang, " năm ", nam, " có ", so_ngay, " ngày.")
