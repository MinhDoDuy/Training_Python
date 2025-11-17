##Bài Tập 1: Tính toán Hình học (Hình tròn)

#1. Định nghĩa bằng số Pi
Pi = 3.14

#2. Yêu cầu người dùng nhập bán kính (R) và ép kiểu sang float
try:
    ban_kinh = float(input("Nhập bán kính (R) của hình tròn: "))
except ValueError:
    print("Lỗi: Đầu vào không hợp lệ. Bán kính phải là một số.")
    #Kết thúc chương trình nếu đầu vào không hợp lệ
    exit()

#3. Tính toán chu vi và diện tích
chu_vi = 2 * Pi * ban_kinh
dien_tich = Pi * (ban_kinh ** 2) #Sử dụng ** 2 để tính R^2

#4. In kết quả ra màn hình với định dạng thân thiện (sử dụng f-String)
print("-" * 30)
print(f"Bán kinh (R): {ban_kinh}")
print(f"Chu vi hình tròn là: {chu_vi: .5f}") #Định dạng lấy 5 chữ số thập phân
print (f"Diện tích của hình tròn là: {dien_tich: .5f}") #Định dạng lấy 5 chữ số thập phân
print("-" * 30)

## Bài tập 2: Thao tác với Chuỗi (Hồ sơ cơ bản)
#1. Thu thập thông tin từ người dùng
ho_ten = input("Nhập Họ và Tên : ")
nghe_nghiep = input("Nhập Nghề Nghiệp : ")
nam_sinh_str = input("Nhập Năm Sinh (Vi du 1995): ")

#2. Tính toán tuổi và xử lý lỗi (Áp dụng kiến thức Ngày 5 một chút)
Nam_Hien_Tai = 2025
try:
    nam_sinh_str = int(nam_sinh_str) #ép kiếu chuỗi năm sinh sang số nguyên
    tuoi = Nam_Hien_Tai - nam_sinh_str
except ValueError:
    tuoi = "Không xác dịnh (Lỗi nhập năm sinh)"
print(f"Tên {ho_ten}, Nghề Nghiệp: {nghe_nghiep}, Tuổi: {tuoi}")

#3. Bài tập 3: Ép Kiểu và Giá trị Logic

# --- Phần A: Ép kiểu sang boolean ---
print("\n--- Phần A: Ép kiểu sang boolean ---")
a = 0           #Số nguyên 0
b = "Python"    #Chuỗi có nội dụng
chuoi_rong = "" #Chuỗi rỗng

print(f"bool (a = 0) là: {bool(a)}")                     #Kết quả: False (0 là Falsy)
print(f"bool (b = 'Python') là: {bool(b)}")              #Kết quả: True (Chuỗi không rỗng là Truthy)
print(f"bool (chuoi_rong = ' ') là: {bool(chuoi_rong)}") #Kết quả: False (Chuỗi rỗng là Falsy)

# --- Phần B: Ép kiểu sang Integer ---
print("\n--- Phần B: Ép kiểu sang Integer ---")
c_true = True
d_false = False

print(f"int (True) là: {int(c_true)}")   #Kết quả: 1
print(f"int (False) là: {int(d_false)}") #Kết quả: 0

# --- Phần C: So Sánh (Kết quả là bool) ---
print("\n--- Phần C: So sánh ---")
try:
    so_nguyen = int(input("Vui lòng nhập một số nguyên bất kỳ: "))
    #Phép so sánh sẽ trả về True hoặc False
    ket_qua_so_sanh = so_nguyen > 100
    print(f"Số vừa nhập ({so_nguyen}) có lớn hơn 100 hay không? Kết quả là: {ket_qua_so_sanh}")
except ValueError:
    print("Lỗi: Đầu vào không phải số nguyên.")











