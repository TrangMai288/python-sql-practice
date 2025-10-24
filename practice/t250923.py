# -------------------------------
# Python cơ bản – Ôn lại cơ bản
# Tác giả: TrangMH
# Ngày: 2025-09-23
#
# Nội dung:
# - Viết chương trình quản lý danh sách số nguyên với yêu cầu sau:
#   + Nhập vào một danh sách số nguyên.
#   + Tính và in ra tổng các số lẻ trong danh sách.
#   + Tìm và in ra giá trị lớn nhất trong danh sách.
#
# -------------------------------
def nhap_danh_sach():
    danh_sach = []
    number = int(input("Nhap so cac phan tu: "))
    for i in range(0, number):
        i = int(input(f"Nhap phan tu thu {i + 1}: "))
        danh_sach.append(i)
    return danh_sach

def so_le(number):
    if number % 2 != 0:
        return True

def tong_cac_so_le(danh_sach):
    tong_so_le = 0
    for i in danh_sach:
        if so_le(i):
            tong_so_le += i
    return tong_so_le

def gia_tri_lon_nhat(danh_sach):
    return max(danh_sach)

def main():
    danh_sach_so_nguyen = nhap_danh_sach()
    print(f"Danh sach so nguyen la: {danh_sach_so_nguyen}")
    tong_so_le = tong_cac_so_le(danh_sach_so_nguyen)
    print(f"Tong cac so le trong danh sach: {tong_so_le}")
    so_lon_nhat = gia_tri_lon_nhat(danh_sach_so_nguyen)
    print(f"Gia tri lon nhat trong danh sach: {so_lon_nhat}")
    
main()

'''
Giả sử bạn có bảng Orders gồm các cột:
- order_id (số nguyên, khóa chính)
- customer_name (chuỗi)
- amount (số thực, tổng tiền đơn hàng)
- order_date (ngày đặt hàng)

Yêu cầu:
- Viết câu lệnh SQL để lấy ra tên khách hàng và tổng số tiền (amount) của họ, 
chỉ tính những khách hàng có tổng tiền lớn hơn 500, sắp xếp theo tổng tiền giảm dần.
SELECT customer_name, SUM(amount)
FROM orders 
GROUP BY customer_name
HAVING SUM(amount) > 500
ORDER BY SUM(amount) DESC
----
- WHERE dùng để lọc trước khi nhóm (từng dòng dữ liệu).
- HAVING dùng để lọc sau khi đã nhóm & tính toán tổng hợp (SUM, AVG, COUNT…).
==========================
Giả sử có bảng Sales với các cột:
- id (số nguyên, khóa chính)
- product (tên sản phẩm)
- category (loại sản phẩm, ví dụ: "Electronics", "Clothing")
- quantity (số lượng bán, số nguyên)
- price (giá bán mỗi sản phẩm, số thực)

Bài 1: Viết câu lệnh SQL để lấy ra tên sản phẩm và tổng doanh thu (quantity * price), 
chỉ lấy những sản phẩm có tổng doanh thu trên 1000, 
kết quả sắp xếp theo tổng doanh thu giảm dần.
Bài 2: Viết câu lệnh SQL để tính tổng số lượng bán theo từng loại sản phẩm (category), 
chỉ hiển thị những loại có tổng số lượng ít nhất 50.
Bài 3: Viết câu lệnh SQL để lấy ra loại sản phẩm (category) và số lượng sản phẩm khác nhau trong loại đó (dùng COUNT(DISTINCT product)), 
chỉ hiển thị các loại có ít nhất 3 sản phẩm khác nhau.

1.
select product as ten_san_pham, sum(quantity * price) as tong_doanh_thu
from sales
group by ten_san_pham
having sum(quantity * price) > 1000
ORDER BY tong_doanh_thu DESC
2.
select category as loai_san_pham, sum(quantity) as tong_so_luong
from sales
group by category
having sum(quantity) >= 50
3.
select category, count(distinct(product)) as so_luong_san_pham
from sales
group by category
having count(distinct(product)) >= 3 
'''