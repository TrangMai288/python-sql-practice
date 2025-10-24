# -------------------------------
# Python cơ bản – Ôn lại cơ bản
# Tác giả: TrangMH
# Ngày: 2025-09-24
#
# Nội dung:
# - Viết chương trình quản lý danh sách điểm thi của sinh viên:
#   + Nhập vào danh sách điểm (số thực, cách nhau bởi dấu cách).
#   + Tính và in ra điểm trung bình.
#   + Đếm xem có bao nhiêu sinh viên điểm >= 8 (giỏi).
#   + Tìm và in ra điểm thấp nhất trong danh sách.
#
# -------------------------------

def nhap_diem():
    danh_sach_diem = []
    so_cac_mon_can_nhap_diem = int(input("Nhap diem cua cac sinh vien: "))
    for i in range(0, so_cac_mon_can_nhap_diem):
        diem = float(input(f"Nhap diem cua sinh vien thu {i + 1}: "))
        danh_sach_diem.append(diem)
    return danh_sach_diem

def tinh_diem_trung_binh(danh_sach):
    tong_diem = 0
    for i in danh_sach:
        tong_diem += i
    diem_trung_binh = tong_diem / len(danh_sach)
    return diem_trung_binh

def loc_diem_sinh_vien(danh_sach):
    so_sinh_vien_diem_lon_hon_bang_8 = 0
    for i in danh_sach:
        if i >= 8:
            so_sinh_vien_diem_lon_hon_bang_8 += 1
    return so_sinh_vien_diem_lon_hon_bang_8

def tim_diem_thap_nhat(danh_sach):
    return min(danh_sach)

def main():
    danh_sach_diem = nhap_diem()
    print(f"Danh sach diem: {danh_sach_diem}")
    diem_trung_binh = tinh_diem_trung_binh(danh_sach_diem)
    print(f"Diem trung binh: {diem_trung_binh:.2f}")
    so_sinh_vien_co_diem_lon_hon_bang_8 = loc_diem_sinh_vien(danh_sach_diem)
    print(f"So sinh vien co diem lon hon bang 8: {so_sinh_vien_co_diem_lon_hon_bang_8}")
    diem_thap_nhat = tim_diem_thap_nhat(danh_sach_diem)
    print(f"Diem thap nhat: {diem_thap_nhat}")
    
main()

'''
Giả sử bảng orders có các cột: order_id, customer_name, amount, order_date.
1. Liệt kê customer_name và trung bình đơn hàng (AVG(amount)), 
chỉ hiển thị khách có trung bình > 300.
2. Liệt kê customer_name và số đơn hàng (COUNT(order_id)), 
chỉ hiển thị khách có từ 5 đơn trở lên.
3. Liệt kê customer_name và đơn hàng cao nhất (MAX(amount)), 
chỉ hiển thị khách có đơn hàng cao nhất > 1000.
------------------
1.
SELECT customer_name, AVG(amount) as trung_binh_don_hang
FROM orders
GROUP BY customer_name
HAVING AVG(amount) > 300
2.
SELECT customer_name, COUNT(order_id) as so_don_hang
FROM orders
GROUP BY customer_name
HAVING COUNT(order_id) >= 5
3.
SELECT customer_name, MAX(amount) as don_hang_cao_nhat
FROM orders
GROUP BY customer_name
HAVING MAX(amount) > 1000
'''