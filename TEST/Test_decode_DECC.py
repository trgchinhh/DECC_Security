from DECC import *

with open("D:\\MA_HOA_PY\\Encode_DECC\\Data_code_mau_da_ma_hoa.txt", mode = "r", encoding = "utf-8") as file:
    noi_dung = file.read()

noi_dung_giai_ma = DECODE(noi_dung = noi_dung, khoa = 3).decode()
print("Ma hoa:", noi_dung_giai_ma)

