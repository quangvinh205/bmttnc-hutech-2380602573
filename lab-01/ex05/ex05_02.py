import re

def tinh_tong_so_trong_chuoi(chuoi):
    cac_so = re.findall(r'-?\d+', chuoi)
    tong_duong = 0
    tong_am = 0
    for so_str in cac_so:
        so = int(so_str)
        if so > 0:
            tong_duong += so
        elif so < 0:
            tong_am += so
    return tong_duong, tong_am

chuoi_nhap = input("Nhập chuỗi: ")
tong_duong, tong_am = tinh_tong_so_trong_chuoi(chuoi_nhap)
print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")

