# -------------------------------
# Python cơ bản – Ôn lại cơ bản
# Tác giả: TrangMH
# Ngày: 2025-09-29
#
# Nội dung:
# - Viết chương trình quản lý sản phẩm trong cửa hàng:
#   + Nhập danh sách sản phẩm gồm tên sản phẩm, giá, số lượng.
#   + Tính giá trị tồn kho của từng sản phẩm (giá * số lượng).
#   + In ra danh sách tất cả sản phẩm kèm giá trị tồn kho.
#   + Tìm sản phẩm có giá trị tồn kho lớn nhất.
#   + In ra danh sách sản phẩm có giá trên giá trung bình.
#
# -------------------------------

def nhap_danh_sach():
    danh_sach = []
    so_luong_san_pham = int(input("Moi ban nhap so san pham se co: "))
    for i in range(0, so_luong_san_pham):
        ten = input(f"Moi ban nhap ten san pham thu {i + 1}: ")
        gia = float(input(f"Moi ban nhap gia san pham thu {i + 1}: "))
        so_luong = int(input(f"Moi ban nhap so luong san pham thu {i + 1}: "))
        san_pham = {"ten": ten, "gia": gia, "so_luong": so_luong}
        danh_sach.append(san_pham)
    return danh_sach

def tinh_gia_tri_ton_kho(danh_sach):
    danh_sach_ton_kho = []
    gia_tri_ton_kho = 0
    for sp in danh_sach:
        gia_tri_ton_kho = sp["gia"] * sp["so_luong"]
        ds_ton_kho = {"ten": sp["ten"], "gia": sp["gia"], "so_luong": sp["so_luong"], "gia tri ton kho": gia_tri_ton_kho}
        danh_sach_ton_kho.append(ds_ton_kho)
    return danh_sach_ton_kho     
    
def tim_gia_tri_ton_kho_lon_nhat(danh_sach):
    gia_tri_ton_kho_lon_nhat = max(x["gia tri ton kho"] for x in danh_sach)
    ds_gia_tri_ton_kho_lon_nhat = []
    for sp in danh_sach:
        if sp["gia tri ton kho"] == gia_tri_ton_kho_lon_nhat:
            ds_gia_tri_ton_kho_lon_nhat.append(sp)
    return ds_gia_tri_ton_kho_lon_nhat
    
def tinh_gia_trung_binh(danh_sach):
    if not danh_sach:
        print("Danh sach rong")
        return []
    tong = 0
    for sp in danh_sach:
        tong += sp["gia"]
    gia_tri_trung_binh = tong / len(danh_sach)
    return gia_tri_trung_binh
            
def tim_san_pham_tren_trung_binh(danh_sach):
    ds_sp_tren_trung_binh = []
    gia_tri_trung_binh = tinh_gia_trung_binh(danh_sach) 
    for sp in danh_sach:
        if sp["gia"] > gia_tri_trung_binh:
            ds_sp_tren_trung_binh.append(sp)
    return ds_sp_tren_trung_binh

def in_danh_sach_gia_tri_ton_kho(danh_sach):
    print("-------------------------------------------------------")
    print(f"{'Ten':<15}{'Gia':>10}{'So Luong':>12}{'Gia tri ton kho':>20}")
    for sp in danh_sach:
        print(f"{sp['ten']:<15}{sp['gia']:>10.2f}{sp['so_luong']:>12}{sp['gia tri ton kho']:>20.2f}")


def main():
    danh_sach_san_pham = nhap_danh_sach()
    danh_sach_gia_tri_ton_kho = tinh_gia_tri_ton_kho(danh_sach_san_pham)
    in_danh_sach_gia_tri_ton_kho(danh_sach_gia_tri_ton_kho)
    ds_san_pham_co_gia_tri_ton_kho_lon_nhat = tim_gia_tri_ton_kho_lon_nhat(danh_sach_gia_tri_ton_kho)
    print(f"Danh sach san pham co gia tri ton kho lon nhat: ")
    in_danh_sach_gia_tri_ton_kho(ds_san_pham_co_gia_tri_ton_kho_lon_nhat)
    
    ds_san_pham_co_gia_tren_trung_binh = tim_san_pham_tren_trung_binh(danh_sach_gia_tri_ton_kho)
    print(f"Danh sach san pham co gia tren gia trung binh: ")
    in_danh_sach_gia_tri_ton_kho(ds_san_pham_co_gia_tren_trung_binh)
    
main()

'''
Cho 2 bảng:
Customers(customer_id, customer_name, city); 
Orders(order_id, customer_id, order_date, amount)
1. Tìm 3 khách hàng có tổng số tiền mua hàng cao nhất trong năm 2024.
2. Tìm khách hàng chưa từng đặt đơn hàng nào.
3. Với mỗi thành phố, cho biết tổng số đơn hàng và trung bình số tiền mỗi đơn. 
Chỉ lấy những thành phố có ít nhất 5 khách hàng khác nhau.
------------------
1.
SELECT c.customer_name, SUM(o.amount) AS total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE YEAR(o.order_date) = 2024
GROUP BY c.customer_name
ORDER BY total_amount DESC
LIMIT 3
2.
SELECT c.customer_name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
3.
SELECT c.city, COUNT(o.order_id) AS total_orders, AVG(o.amount) AS avg_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING COUNT(DISTINCT c.customer_name) >= 5
'''