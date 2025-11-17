## Bài Tập 1: Phân loại Thu nhập

try:
    # Ép kiểu đầu vào thành số nguyên
    thu_nhap = int(input("Vui lòng nhập mức thu nhập hàng tháng (VND): "))

    # 1. Phân loại và in ra mức thuế suất
    if thu_nhap <= 0:
        print("Thu nhập không hợp lệ (phải là số dương > 0).")
    elif thu_nhap <= 10000000:
        # Thu nhập < 10,000,000
        print(f"Thu nhập {thu_nhap:,} VND: Miễn thuế (0%).")
    elif thu_nhap <= 20000000:
        # Thu nhập 10,000,001 - 20,000,000
        print(f"Thu nhập {thu_nhap:,} VND: Thuế suất thấp (5%).")
    elif thu_nhap <= 50000000:
        # Thu nhập 20,000,001 - 50,000,000
        print(f"Thu nhập {thu_nhap:,} VND: Thuế suất trung bình (10%).")
    else:
        # Thu nhập > 50,000,000
        print(f"Thu nhập {thu_nhap:,} VND: Thuế suất cao (20%).")

except ValueError:
    print("Lỗi: Đầu vào không phải là một số nguyên hợp lệ.")
# Lưu ý: {thu_nhap:,} là cách định dạng số có dấu phẩy phân cách hàng nghìn.

print("---------------------------------------------")

## Bài Tập 2: Phân tích List
# --- Nhập danh sách số từ bàn phím ---
# danh_sach_so = input("Nhập danh sách số, cách nhau bằng dấu cách: ")
# danh_sach_so = [int(so) for so in danh_sach_so.split()]

danh_sach_so = [12, 7, 21, 14, 5, 30, 18, 9]
tong_so_le = 0
cac_so_le = []
tong_so_chan = 0
cac_so_chan = []
dem_chia_het_cho_3 = 0
so_chia_het_cho_3 = []

print(f"List ban đầu: {danh_sach_so}")

for so in danh_sach_so:
    # 1. Tính Tổng các số lẻ
    if so % 2 != 0:
        tong_so_le += so
        cac_so_le.append(so)
    else:  # 2. Tính tổng các số chẵn
        tong_so_chan += so
        cac_so_chan.append(so)

    # 2. Đếm và Lọc các số chia hết cho 3
    if so % 3 != 0:
        continue  # Nếu không chia hết cho 3, bỏ qua đoạn code dưới và chuyển sang vòng lặp kế tiếp

    # Nếu code chạy đến đây, nghĩa là số đó chia hết cho 3
    dem_chia_het_cho_3 += 1
    so_chia_het_cho_3.append(so)

print("\n--- Kết quả Phân tích ---")
print(f"1. Tổng các số lẻ trong List là: {tong_so_le}")
print(f"    Các số lẻ là: {cac_so_le}")
print(f"2. Tổng các số chẵn trong list là: {tong_so_chan}")
print(f"    Các số lẻ là: {cac_so_chan}")
print(f"3. Số lượng số chia hết cho 3: {dem_chia_het_cho_3}")
print(f"   Các số chia hết cho 3 là: {so_chia_het_cho_3}")
print("---------------------------------------------")

## Bài Tập 3: Trò chơi Đoán Mật khẩu

MAT_KHAU_BI_MAT = "minh"
SO_LAN_THU_TOI_DA = 3
lan_thu_hien_tai = 0
dang_nhap_thanh_cong = False

print(f"Bạn có {SO_LAN_THU_TOI_DA} lần thử để đăng nhập.")

# Sử dụng vòng lặp while để kiểm soát số lần thử
while lan_thu_hien_tai < SO_LAN_THU_TOI_DA:
    lan_thu_hien_tai += 1

    mat_khau_nhap = input(f"Lần thử thứ {lan_thu_hien_tai}: Nhập mật khẩu: ")

    if mat_khau_nhap == MAT_KHAU_BI_MAT:
        print("✅ Đăng nhập thành công! Chào mừng bạn.")
        dang_nhap_thanh_cong = True
        break  # Dùng break để thoát khỏi vòng lặp ngay lập tức
    else:
        so_lan_con_lai = SO_LAN_THU_TOI_DA - lan_thu_hien_tai
        if so_lan_con_lai > 0:
            print(f"❌ Mật khẩu sai. Bạn còn {so_lan_con_lai} lần thử.")
        else:
            print("❌ Mật khẩu sai.")

# Kiểm tra sau khi vòng lặp kết thúc
if not dang_nhap_thanh_cong:
    print("\n🚨 TÀI KHOẢN CỦA BẠN ĐÃ BỊ KHÓA do nhập sai quá số lần quy định.")