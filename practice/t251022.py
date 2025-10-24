# -------------------------------
# Python cơ bản – Ôn lại cơ bản
# Tác giả: TrangMH
# Ngày: 2025-10-22
#
# Nội dung:
# - Viết chương trình quản lý điểm thi của học sinh với yêu cầu:
#   + Nhập danh sách học sinh gồm: tên, điểm toán, điểm anh, điểm lý.
#   + Tính điểm trung bình mỗi học sinh và lưu vào danh sách.
#   + Tìm học sinh có điểm trung bình cao nhất.
#   + In ra danh sách học sinh có điểm trung bình trên trung bình của lớp.
#
# -------------------------------

def nhap_so_hoc_sinh():
    while True:
        try:
            so_hoc_sinh = int(input("Moi ban nhap so hoc sinh: ")) 
            if so_hoc_sinh <= 0:
                print("→ So hoc sinh phai lon hon 0!")
            else:
                return so_hoc_sinh
        except ValueError:
            print("→ Vui long nhap so hop le!")
        
def nhap_ten(so_thu_tu):
    while True:
        try:
            ten = input(f"Moi ban nhap ten hoc sinh thu {so_thu_tu}: ")
            if ten.strip() == "":
                print("→ Ban can nhap ten!")
            else:
                return ten
        except ValueError:
            print("→ Vui long nhap ten hop le!")
            
def nhap_diem(mon):
    while True:
        try:
            diem = float(input(f"Moi ban nhap diem mon {mon}: "))
            if diem < 0 or diem > 10:
                print("→ Diem phai trong khoang [0 - 10]")
            else:
                return diem
        except ValueError:
            print("→ Vui long nhap so hop le!")

def nhap_danh_sach():
    so_hoc_sinh = nhap_so_hoc_sinh()
    danh_sach_hoc_sinh = []
    
    for i in range(0, so_hoc_sinh):
        ten = nhap_ten(i + 1)
        toan = nhap_diem("Toan")
        anh = nhap_diem("Anh")
        ly = nhap_diem("Ly")
        diem_thi = {"ten": ten, "toan": toan, "anh": anh, "ly": ly}
        danh_sach_hoc_sinh.append(diem_thi)
    return danh_sach_hoc_sinh

def tinh_diem_trung_binh(danh_sach):
    danh_sach_diem_trung_binh = []
    for hs in danh_sach:
        tong_diem = hs["toan"] + hs["anh"] + hs["ly"]
        diem_trung_binh = tong_diem / 3
        diem_tb = {"ten": hs['ten'], "toan": hs['toan'], "anh": hs['anh'], "ly": hs['ly'], "diem_tb": diem_trung_binh}
        danh_sach_diem_trung_binh.append(diem_tb)
    return danh_sach_diem_trung_binh

def tinh_diem_trung_binh_cao_nhat(danh_sach):
    diem_trung_binh_cao_nhat = max(x['diem_tb'] for x in danh_sach)
    ds_hoc_sinh_co_diem_tb_cao_nhat = []
    for i in danh_sach:
        if diem_trung_binh_cao_nhat == i["diem_tb"]:
            ds_hoc_sinh_co_diem_tb_cao_nhat.append(i['ten'])
    return ds_hoc_sinh_co_diem_tb_cao_nhat

def tinh_diem_trung_binh_cua_lop(danh_sach):
    tong_diem_trung_binh_cua_lop = sum(x['diem_tb'] for x in danh_sach)
    diem_trung_binh_cua_lop = tong_diem_trung_binh_cua_lop / len(danh_sach)
    return diem_trung_binh_cua_lop

def tim_danh_sach_hoc_sinh_tren_trung_binh(danh_sach):
    diem_tb_cua_lop = tinh_diem_trung_binh_cua_lop(danh_sach)
    ds_hoc_sinh_tren_trung_binh = []
    for hs in danh_sach:
        if hs['diem_tb'] > diem_tb_cua_lop:
            ds_hoc_sinh_tren_trung_binh.append(hs['ten'])
    return ds_hoc_sinh_tren_trung_binh

def in_danh_sach_day_du(danh_sach):
    if not danh_sach:
        print("Danh sach rong")
        return []
    print("=" * 65)
    print(f"{'Ten':<15}{'| Diem toan':>12}{'| Diem anh':>12}{'| Diem ly':>12}{' | Diem TB':>13}")
    print("-" * 65)
    for hs in danh_sach:
        print(f"{hs['ten']:<15} | {hs['toan']:>10.2f} | {hs['anh']:>10.2f} | {hs['ly']:>10.2f} | {hs['diem_tb']:>6.2f}")

def in_danh_sach(danh_sach, tu_khoa):
    if not danh_sach:
        print("Danh sach rong")
        return []
    print("=" * 65)
    if(tu_khoa == "tb cao nhat"):
        print("Danh sach hoc sinh co diem trung binh cao nhat: ")
    elif(tu_khoa == "ds hoc sinh tren trung binh"):
        print("Danh sach hoc sinh co diem trung binh tren trung binh cua lop: ")
    else:
        print("Sai tu khoa!")    
    for i in danh_sach:
        print(i)

def in_danh_sach_tren_tb(danh_sach):
    if not danh_sach:
        print("Danh sach rong")
        return []
    print("=" * 65)
    print("Học sinh có điểm trung bình trên trung bình của lớp:")
    for ten in danh_sach:
        print(f"- {ten}")

def main():
    danh_sach_diem_thi_hoc_sinh = nhap_danh_sach()
    ds_diem_tb = tinh_diem_trung_binh(danh_sach_diem_thi_hoc_sinh)
    
    in_danh_sach_day_du(ds_diem_tb)
    
    ds_hoc_sinh_co_diem_tb_cao_nhat = tinh_diem_trung_binh_cao_nhat(ds_diem_tb)
    ds_hoc_sinh_tren_trung_binh = tim_danh_sach_hoc_sinh_tren_trung_binh(ds_diem_tb)
    
    in_danh_sach(ds_hoc_sinh_co_diem_tb_cao_nhat, "tb cao nhat")
    in_danh_sach_tren_tb(ds_hoc_sinh_tren_trung_binh)
    
main()

'''
Cho 2 bảng:
Employees(emp_id, emp_name, dept_id, salary); 
Departments(dept_id, dept_name)
1. Tìm tên phòng ban có mức lương trung bình cao nhất.
2. Liệt kê nhân viên có mức lương cao hơn mức trung bình của phòng ban họ làm việc.
3. Tính số nhân viên mỗi phòng ban, 
chỉ hiển thị những phòng ban có trên 3 nhân viên và lương trung bình > 6000, 
sắp xếp theo lương trung bình giảm dần.
------------------
1. 
SELECT d.dept_name, AVG(e.salary) as avg_salary
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY avg_salary DESC
LIMIT 1
2. 
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > (SELECT AVG(e2.salary) 
FROM employees e2
WHERE e2.dept_id = e.dept_id)
3. 
SELECT d.dept_name, COUNT(e.emp_id) as so_nhan_vien, AVG(e.salary) as luong_trung_binh
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id)> 3 AND AVG(e.salary) > 6000
ORDER BY luong_trung_binh DESC
'''