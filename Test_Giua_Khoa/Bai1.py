n = input("Nhap day so: ")
so = tuple(map(int, n.split()))
for x in set(n):
    if n.count(x) % 5 == 0 and n.count(x) % 10 !=0:
        print(x , end = ' ')