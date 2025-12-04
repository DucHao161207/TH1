n = int(input())
if 0 < n < 100:
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    print(giai_thua)
else:
    print("Nhap sai du lieu")