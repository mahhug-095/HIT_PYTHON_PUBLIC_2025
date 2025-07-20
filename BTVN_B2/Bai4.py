tien = int(input("Nhập số xu: "))
gia_1_chai = 28

chai = tien // gia_1_chai
chai_rong = chai
while chai_rong >= 3:
    chai_moi = chai_rong // 3
    chai += chai_moi
    chai_rong = chai_rong % 3 + chai_moi
print(f"Số chai bia có thể mua được là: {chai}")
