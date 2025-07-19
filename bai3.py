n = int(input("nhập số: "))
dem = 0
bien = abs(n)
tong = 0
while bien > 0:
    chu_so = bien % 10
    tong += chu_so
    bien //= 10
    dem += 1
print(n, " có ", dem, " chữ số tổng các chữ số là: ", tong)
