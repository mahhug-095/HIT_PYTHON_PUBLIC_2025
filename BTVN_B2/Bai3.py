n = int(input("Nhập n: "))
so_chu_so = 0
tong_chu_so = 0
while n > 0:
    chu_so = n % 10
    tong_chu_so += chu_so
    so_chu_so += 1
    n //= 10
print(f"Số chữ số: {so_chu_so} Tổng chữ số: {tong_chu_so}")