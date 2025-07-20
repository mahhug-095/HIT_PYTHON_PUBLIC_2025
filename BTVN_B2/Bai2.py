luong = int(input("Nhập lương: "))
if luong >= 15000000:
    thue = luong * 0.3
elif luong >= 7000000:
    thue = luong * 0.2
else:
    thue = luong * 0.1
thunhap = luong - thue
print(f"Thuế: {int(thue)} Thu nhập: {int(thunhap)}")