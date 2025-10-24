# -------------------------------
# Python cơ bản – Ôn lại cơ bản
# Tác giả: TrangMH
# Ngày: 2025-09-19
#
# Nội dung:
# - Viết một chương trình quản lý danh sách số nguyên với các chức năng sau:
#   + Nhập vào một danh sách số nguyên (từ người dùng, cách nhau bởi dấu cách).
#   + In ra danh sách sau khi đã sắp xếp tăng dần.
#   + Đếm và in ra số lượng phần tử chẵn trong danh sách.
#
# Kết quả:
# - Ôn lại cách nhập dữ liệu từ bàn phím với input() và xử lý với list.
# - Hiểu rõ sự khác biệt giữa list.sort() (thay đổi trực tiếp) và sorted() (trả về list mới).
# - Viết chương trình tách hàm, tổ chức code rõ ràng hơn.
# - Củng cố kỹ năng dùng vòng lặp và điều kiện để xử lý chẵn/lẻ.
# -------------------------------
def nhap_danh_sach():
    danh_sach_so_nguyen = []
    number = int(input("Nhap so cac phan tu: "))
    for i in range(0, number):
        so_nguyen = int(input(f"Nhap so nguyen thu {i + 1}: "))
        danh_sach_so_nguyen.append(so_nguyen)
    return danh_sach_so_nguyen
    
def danh_sach_sap_xep_tang_dan(danh_sach):
    danh_sach.sort()

def in_danh_sach(danh_sach):
    print(f"Danh sach cac so nguyen la: {danh_sach}")
        
def dem_so_phan_tu_chan(danh_sach):
    so_phan_tu_chan = 0
    for i in danh_sach:
        if i % 2 == 0:
            so_phan_tu_chan += 1
    print(f"So phan tu chan: {so_phan_tu_chan}")
 
def in_ra_so_phan_tu_chan(danh_sach):
    danh_sach_phan_tu_chan = []
    for i in danh_sach:
        if i % 2 == 0:
            danh_sach_phan_tu_chan.append(i)
    print(f"Danh sach cac phan tu chan: {danh_sach_phan_tu_chan}")
       
def main():
    danh_sach = nhap_danh_sach()
    danh_sach_sap_xep_tang_dan(danh_sach)
    in_danh_sach(danh_sach)
    dem_so_phan_tu_chan(danh_sach)
    in_ra_so_phan_tu_chan(danh_sach)
    
main()