thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
if nam <= 0 or thang <= 0 or thang >= 12:
    print("Khong ton tai")
else:
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print("31 ngay")
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        print("30 ngay")
    else: 
        if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
            print("29 ngay")
        else:
            print("28 ngay")
