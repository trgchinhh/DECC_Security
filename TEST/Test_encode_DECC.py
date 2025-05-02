from DECC import *

with open("D:\\MA_HOA_PY\\Encode_DECC\\Code_mau.py", mode = "r", encoding = "utf-8") as file:
    noi_dung = file.read()

noi_dung_ma_hoa = ENCODE(noi_dung = noi_dung, khoa = 3).encode()
print("Ma hoa:", noi_dung_ma_hoa)

