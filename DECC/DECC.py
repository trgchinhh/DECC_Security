import random

mang_chu_cai = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\', ';', ':', '"', '\'', '<', '>', ',', '.',
    '/', '?', '`', '~', ' ', '\n', '\t'
]

khoa_cho_phep = [1, 2, 3, 4]

class ENCODE:
    def __init__(self, noi_dung, khoa):
        self.noi_dung = noi_dung
        self.khoa = khoa
        if(self.khoa not in khoa_cho_phep):
            raise BaseException("Khoa cho phep gom [1, 2, 3, 4]")

    def encode_xor(self, noi_dung):
        ket_qua = ""
        for i in range(len(noi_dung)):
            ket_qua += chr(ord(noi_dung[i]) ^ self.khoa)
        return ket_qua

    def encode_caesar(self, noi_dung):
        ket_qua = ""
        for ky_tu in noi_dung:
            if ky_tu in mang_chu_cai:
                vi_tri = mang_chu_cai.index(ky_tu)
                vi_tri_moi = (vi_tri + self.khoa) % len(mang_chu_cai)
                ket_qua += mang_chu_cai[vi_tri_moi]
            else:
                ket_qua += ky_tu  # Nếu ký tự không có trong danh sách, giữ nguyên
        return ket_qua

    def encode(self):
        noi_dung_xor = self.encode_xor(self.noi_dung)
        noi_dung_ma_hoa = self.encode_caesar(noi_dung_xor)
        return noi_dung_ma_hoa


class DECODE:
    def __init__(self, noi_dung, khoa):
        self.noi_dung = noi_dung
        self.khoa = khoa
        if(self.khoa not in khoa_cho_phep):
            raise BaseException("Khoa cho phep gom [1, 2, 3, 4]")

    def decode_xor(self, noi_dung):
        ket_qua = ""
        for i in range(len(noi_dung)):
            ket_qua += chr(ord(noi_dung[i]) ^ self.khoa)
        return ket_qua

    def decode_caesar(self, noi_dung):
        ket_qua = ""
        for ky_tu in noi_dung:
            if ky_tu in mang_chu_cai:
                vi_tri = mang_chu_cai.index(ky_tu)
                vi_tri_goc = (vi_tri - self.khoa) % len(mang_chu_cai)
                ket_qua += mang_chu_cai[vi_tri_goc]
            else:
                ket_qua += ky_tu
        return ket_qua

    def decode(self):
        noi_dung_caesar = self.decode_caesar(self.noi_dung)
        noi_dung_giai_ma = self.decode_xor(noi_dung_caesar)
        return noi_dung_giai_ma
