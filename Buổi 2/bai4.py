n = int(input("nhập số xu: "))
mua = n//28
chai = mua
vo = mua
while vo > 3:
    doi = vo//3
    chai += doi
    vo = vo % 3+doi
print(chai)
