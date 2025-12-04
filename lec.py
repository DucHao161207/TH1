def chia_lam_tron_xuong(m, n):
    if n == 0:
        return "Không thể chia cho 0"
    ket_qua = m // n
    return ket_qua
try:
    m = int(input("Nhập số bị chia m: "))
    n = int(input("Nhập số chia n: "))
    print(f"Kết quả làm tròn xuống của {m} / {n} là: {chia_lam_tron_xuong(m, n)}")
except ValueError:
    print("Vui lòng nhập số nguyên.")