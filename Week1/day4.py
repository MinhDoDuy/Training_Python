## Bài Tập 1: Hàm Tính Toán Cơ bản

def tinh_tong_hieu(so_a, so_b):
    """
    Hàm tính Tổng và Hiệu của hai số.
    :param so_a: Số thứ nhất (int/float)
    :param so_b: Số thứ hai (int/float)
    :return: Tuple chứa (Tổng, Hiệu) của so_a và so_b
    """
    tong = so_a + so_b
    hieu = so_a - so_b

    # Trả về cả hai kết quả. Python tự động đóng gói thành một Tuple
    return tong, hieu


# --- Kiểm tra và in kết quả ---

# 1. Gọi hàm và nhận Tuple kết quả
ket_qua_tuple = tinh_tong_hieu(10, 5)
print(f"Kết quả trả về (Tuple): {ket_qua_tuple}")

# 2. Bóc tách Tuple thành các biến riêng biệt (Tuple Unpacking)
tong_so, hieu_so = tinh_tong_hieu(10, 5)

print("-" * 20)
print(f"Input: 10, 5")
print(f"Tổng là: {tong_so}")  # 15
print(f"Hiệu là: {hieu_so}")  # 5

# Ví dụ khác
tong_moi, hieu_moi = tinh_tong_hieu(25.5, 12.5)
print("-" * 20)
print(f"Input: 25.5, 12.5")
print(f"Tổng là: {tong_moi}")  # 38.0
print(f"Hiệu là: {hieu_moi}")  # 13.0
print("-" * 30)


## Bài Tập 2: Hàm Kiểm tra Điều kiện

def kiem_tra_nam_nhuan(nam):
    """
    Kiểm tra xem một năm có phải là năm nhuận hay không.
    Quy tắc: (Chia hết cho 4 VÀ không chia hết cho 100) HOẶC (Chia hết cho 400).
    :param nam: Năm cần kiểm tra (int)
    :return: True nếu là năm nhuận, False nếu không.
    """

    # Sử dụng toán tử logic 'and' và 'or'
    la_nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

    return la_nam_nhuan


# --- Kiểm tra và in kết quả ---

nam_hien_tai = 2026
nam_nhuan_gan_nhat = 2500
nam_nhuan_dac_biet = 2000
nam_khong_nhuan = 1900

print(f"Năm {nam_hien_tai}: Năm nhuận? -> {kiem_tra_nam_nhuan(nam_hien_tai)}")  # False
print(f"Năm {nam_nhuan_gan_nhat}: Năm nhuận? -> {kiem_tra_nam_nhuan(nam_nhuan_gan_nhat)}")  # True
print(f"Năm {nam_nhuan_dac_biet}: Năm nhuận? -> {kiem_tra_nam_nhuan(nam_nhuan_dac_biet)}")  # True (vì chia hết cho 400)
print(
    f"Năm {nam_khong_nhuan}: Năm nhuận? -> {kiem_tra_nam_nhuan(nam_khong_nhuan)}")  # False (vì chia hết cho 100, nhưng không chia hết cho 400)
print("-" * 30)


## Bài Tập 3: Hàm Thao tác với List

# Giữ nguyên hàm tính trung bình đã viết ở Ngày 4
def tinh_trung_binh_list(danh_sach_so):
    """Tính giá trị trung bình của List các số."""
    so_luong = len(danh_sach_so)

    if so_luong == 0:
        return 0

    tong = 0
    for so in danh_sach_so:
        tong += so

    trung_binh = tong / so_luong
    return trung_binh


# ----------------------------------------------------
# --- Phần MỚI: Nhập và Xử lý Data từ User (Dùng Dấu Cách) ---

# 1. Nhận đầu vào từ người dùng
du_lieu_nhap = input("Vui lòng nhập một dãy số cách nhau bởi DẤU CÁCH (ví dụ: 10 20 30 40): ")

# 2. Tách chuỗi thành một List các CHUỖI bằng .split() không đối số
# '10 20 30' -> ['10', '20', '30']
# '10   20'  -> ['10', '20']
list_chuoi = du_lieu_nhap.split()

list_so_nguyen = []

for item_chuoi in list_chuoi:
    # item_chuoi đã được .split() làm sạch khoảng trắng đầu cuối, nhưng ta vẫn dùng try-except để bắt lỗi ép kiểu
    if item_chuoi:  # Đảm bảo chuỗi không rỗng
        try:
            # Ép kiểu từ chuỗi sang số nguyên (int)
            so = int(item_chuoi)
            list_so_nguyen.append(so)
        except ValueError:
            print(f"Cảnh báo: Bỏ qua giá trị không hợp lệ: '{item_chuoi}'")

# 3. Gọi hàm với List đã được làm sạch
trung_binh_cuoi_cung = tinh_trung_binh_list(list_so_nguyen)

# 4. In kết quả cuối cùng
print("-" * 50)
print(f"Danh sách các số hợp lệ đã nhập: {list_so_nguyen}")
print(f"Giá trị trung bình của danh sách là: {trung_binh_cuoi_cung}")
print("-" * 50)
