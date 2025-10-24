# -------------------------------
# Python cơ bản – Ôn lại cơ bản
# Tác giả: TrangMH
# Ngày: 2025-09-24
#
# Nội dung:
# - Viết chương trình quản lý danh sách sinh viên với các yêu cầu:
#   + Nhập vào tên và điểm của n sinh viên (dùng list chứa tuple/dict).
#   + In ra danh sách sinh viên.
#   + Tính và in ra điểm trung bình của cả lớp.
#   + In ra danh sách những sinh viên có điểm trên trung bình.
#   + Tìm và in ra sinh viên có điểm cao nhất.
#
# -------------------------------
def nhap_ten_va_diem():
    danh_sach_sinh_vien = []
    so_sinh_vien = int(input("Moi ban nhap so sinh vien: "))
    for i in range(0, so_sinh_vien):
        ten = input(f"Moi ban nhap ten sinh vien thu {i + 1}: ")
        diem = float(input(f"Moi ban nhap diem sinh vien thu {i + 1}: "))
        sinh_vien = {"ten": ten, "diem": diem}
        danh_sach_sinh_vien.append(sinh_vien)
    return danh_sach_sinh_vien

def tinh_diem_trung_binh(danh_sach):
    if not danh_sach:
        return 0
    tong_diem = 0
    for i in danh_sach:
        tong_diem += i["diem"]
    so_sinh_vien = len(danh_sach)
    diem_trung_binh = tong_diem / so_sinh_vien
    return diem_trung_binh

def lay_danh_sach_sinh_vien_co_diem_tren_trung_binh(danh_sach):
    if not danh_sach:
        return []
    danh_sach_sinh_vien_co_diem_tren_trung_binh = []
    diem_trung_binh = tinh_diem_trung_binh(danh_sach)
    for i in danh_sach:
        if i["diem"] > diem_trung_binh:
            danh_sach_sinh_vien_co_diem_tren_trung_binh.append(i)
    return danh_sach_sinh_vien_co_diem_tren_trung_binh

def tim_sinh_vien_co_diem_cao_nhat(danh_sach):
    # ds_diem = []
    # for i in danh_sach:
    #     ds_diem.append(i['diem'])
    # diem_cao_nhat = max(ds_diem)
    if not danh_sach:
        return []
    diem_cao_nhat = max(i['diem'] for i in danh_sach)
    ds_sv_co_diem_cao_nhat = [] # cho truong hop co nhieu hon 2 nguoi cung diem cao
    for i in danh_sach:
        if i['diem'] == diem_cao_nhat:
            ds_sv_co_diem_cao_nhat.append(i)
    return ds_sv_co_diem_cao_nhat

def in_danh_sach_sinh_vien(danh_sach):
    if not danh_sach:
        print("Khong co du lieu sinh vien.")
        return []
    for i in danh_sach:
        print(f"Ten: {i['ten']}, Diem: {i['diem']}")

def in_diem_trung_binh(number):
    print(f"Diem trung binh: {number:.2f}")
 
def in_sinh_vien_co_diem_cao_nhat(danh_sach):
    if not danh_sach:
        print("Khong co du lieu sinh vien.")
        return []
    print(f"Sinh vien co diem cao nhat:")
    for i in danh_sach:
        print(f"Ten: {i['ten']}, Diem: {i['diem']}")
    
def main():
    danh_sach_sinh_vien = []
    while True:
        print("\n===== MENU =====")
        print("1. Nhập sinh viên")
        print("2. In danh sách sinh viên")
        print("3. In điểm trung bình")
        print("4. In sinh viên có điểm trên trung bình")
        print("5. In sinh viên có điểm cao nhất")
        print("0. Thoát")
        
        chon = input("Moi ban chon: ")
        
        match chon:
            case "1":
                danh_sach_sinh_vien = nhap_ten_va_diem()
            case "2":
                print("Danh sach sinh vien")
                in_danh_sach_sinh_vien(danh_sach_sinh_vien)
            case "3":  
                diem_trung_binh = tinh_diem_trung_binh(danh_sach_sinh_vien)
                if diem_trung_binh > 0:
                    in_diem_trung_binh(diem_trung_binh)
            case "4": 
                danh_sach_sinh_vien_co_diem_tren_trung_binh = lay_danh_sach_sinh_vien_co_diem_tren_trung_binh(danh_sach_sinh_vien)
                print("Danh sach sinh vien co diem tren trung binh")
                in_danh_sach_sinh_vien(danh_sach_sinh_vien_co_diem_tren_trung_binh)
            case "5": 
                sv_co_diem_cao_nhat = tim_sinh_vien_co_diem_cao_nhat(danh_sach_sinh_vien)
                in_sinh_vien_co_diem_cao_nhat(sv_co_diem_cao_nhat)
            case "0": 
                break
            case _:
                print("Moi ban nhap cac so hop le tu 0 → 5.")
    
main()

'''
Dùng bảng orders(order_id, customer_name, product, amount):
1. Tìm những khách hàng có tổng số tiền > 2000 và đồng thời số đơn hàng >= 3.
2. Tìm sản phẩm (product) có giá trị đơn hàng trung bình > 500.
3. Với từng khách hàng, tìm đơn hàng cao nhất 
nhưng chỉ lấy những khách hàng có trung bình đơn hàng > 400
------------------
1.
SELECT customer_name
FROM orders
GROUP BY customer_name
HAVING SUM(amount) > 2000 AND COUNT(order_id) >= 3
2.
SELECT product
FROM orders
GROUP BY product
HAVING AVG(amount) > 500
3.
SELECT customer_name, MAX(amount)
FROM orders
GROUP BY customer_name
HAVING AVG(amount) > 400
'''