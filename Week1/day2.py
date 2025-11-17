## Bài Tập 1: Thao tác cơ bản với List (Quản lý Điểm số)

diem_so = [85, 92, 78, 95, 88]
print(f"List điểm số ban đầu: {diem_so}")

# 1. Truy cập: In ra điểm đầu và điểm cuối
print(f"Điểm đầu tiên: {diem_so[0]}")
print(f"Điểm cuối cùng (sử dụng indexing âm): {diem_so[-1]}")

# 2. Slicing: Ba điểm số ở giữa (từ chỉ số 1 đến 4, không bao gồm 4)
ba_diem_giua = diem_so[1:4]
print(f"Ba điểm số ở giữa: {ba_diem_giua}")

# 3. Sửa đổi: Thêm điểm số mới (90) vào cuối List
diem_so.append(90)
print(f"List sau khi thêm 90: {diem_so}")

# 4. Cập nhật: Sửa điểm 78 thành 80
# Tìm vị trí (chỉ số) của điểm 78
vi_tri_78 = diem_so.index(78)
diem_so[vi_tri_78] = 80
print(f"List sau khi sửa 78 thành 80: {diem_so}")

# 5. Sắp xếp: Sắp xếp List theo thứ tự tăng dần
diem_so.sort() # Sắp xếp trực tiếp trên List diem_so
print(f"List sau khi sắp xếp tăng dần: {diem_so}")

print("------------------------------------")


## Bài Tập 2: Sử dụng Tuple (Dữ liệu cố định)
thong_tin_nhan_vien = ("Nguyen Van A", "Nhan su", 45000000, "Ha Noi")

# 1. Truy cập tên và mức lương
print(f"Tên nhân viên: {thong_tin_nhan_vien[0]}")
print(f"Mức lương: {thong_tin_nhan_vien[2]} VND")

# 2. Lặp: In từng phần tử kèm chỉ số
print("\n--- In từng phần tử trong Tuple ---")
# enumerate() cung cấp cả chỉ số (i) và giá trị (phan_tu) trong vòng lặp
for i, phan_tu in enumerate(thong_tin_nhan_vien):
    print(f"Phần tử {i}: {phan_tu}")

# 3. Kiểm tra tính bất biến (Gây ra lỗi):
print("\n--- Kiểm tra tính bất biến ---")
try:
    thong_tin_nhan_vien[1] = "IT"
except TypeError as e:
    print(f"Lỗi xảy ra: {e}")
    print("**Giải thích:** Tuple là cấu trúc bất biến (immutable). Chúng ta không thể thay đổi giá trị của một phần tử sau khi nó được tạo ra.")


## Bài Tập 3: Thao tác với Dictionary (Quản lý Kho hàng)
kho_hang = {"Laptop": 15, "Chuot": 50, "Ban Phim": 25}
print(f"Kho hàng ban đầu: {kho_hang}")

# 1. Thêm: Thêm một mặt hàng mới
kho_hang["Tai Nghe"] = 40
print(f"Kho hàng sau khi thêm Tai Nghe: {kho_hang}")

# 2. Cập nhật: Tăng số lượng Laptop
kho_hang["Laptop"] += 5
print(f"Kho hàng sau khi cập nhật Laptop: {kho_hang}")

# 3. Truy cập an toàn: Sử dụng .get()
ten_mat_hang = input("\nNhập tên mặt hàng muốn kiểm tra: ")
# Sử dụng .get(key, default_value): nếu key không tồn tại, nó trả về 0 thay vì lỗi KeyError
so_luong_ton = kho_hang.get(ten_mat_hang, 0)

if so_luong_ton > 0:
    print(f"Số lượng tồn kho của {ten_mat_hang}: {so_luong_ton}")
else:
    print(f"Mặt hàng '{ten_mat_hang}' không có trong kho hoặc đã hết.")

# 4. In danh sách: Dùng vòng lặp for để duyệt qua các key và value
print("\n--- Danh sách tồn kho chi tiết ---")
for mat_hang, so_luong in kho_hang.items():
    print(f"[{mat_hang}]: {so_luong}")