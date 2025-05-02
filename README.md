# DECC BOT TELEGRAM (DECODE ENCODE CHINHCIPHER)

![image](https://github.com/user-attachments/assets/d05a895d-8da4-4527-bf50-e9f77d5bac5b)

## Giới thiệu
Bot telegram có khả năng mã hóa file các loại tệp có chữ, nhất là file code như file.py (python), file.cpp (c++), file.js (javascript) ,... Nó sẽ mã hóa dữ liệu thành dạng khó đọc và không thể hiểu (không hỗ trợ chạy file khi đã mã hóa như 1 vài loại mã hóa khác như base64, ...)

## Chức năng
- Bot sẽ không hiểu các lệnh ngoài lệnh /start
- Chỉ hiểu khi tải file lên 
- Liệt kê các thông tin file
- Cho người dùng chọn giữa mã hóa file và giải mã file
- Cho người dùng chọn khóa để mã hóa 

## Yêu cầu
- Python 3.x
- Không cần cài thư viện ngoài 

## Setup
- Khi dùng thì tải cả folder để tránh thiếu tệp 

## Lưu ý
- Cập nhật `BOT_TOKEN` trong mã nguồn để sử dụng bot
- Khóa giữa mỗi file mã hóa và giải mã cùng nhau phải giống nhau (nếu khác thì giải mã sai)
- Mã hóa nhằm mục đích tránh dịch ngược file và bị đánh cắp file không mong muốn 
- Khi chạy file sau mã hóa máy sẽ không hiểu 
- Muốn chạy file sau mã hóa thì phải dịch ngược lại bằng bot 

# Screenshot 

## File gốc:
![image](https://github.com/user-attachments/assets/6a30d8f3-4ec6-45b1-b7e9-5cf9661de2b7)

https://github.com/trgchinhh/DECC_Security/blob/main/TEST/Code_mau.py
## File đã mã hóa:
![image](https://github.com/user-attachments/assets/8371f384-8cb7-4143-8bde-a89828ccec76)

https://github.com/trgchinhh/DECC_Security/blob/main/TEST/Data_code_mau_da_ma_hoa.txt
## File đã giải mã:
 + Mã hóa chưa chuẩn nên còn sai vài ký tự 

![image](https://github.com/user-attachments/assets/d003f36e-4628-43cc-b585-5e976d07fdf4)

https://github.com/trgchinhh/DECC_Security/blob/main/TEST/Data_code_mau_da_giai_ma.txt
## Cách mã hóa file:
![image](https://github.com/user-attachments/assets/e10e6fff-2e31-4e48-9402-d43950a59d9e)

https://github.com/trgchinhh/DECC_Security/blob/main/TEST/Test_encode_DECC.py
## Cách giải mã file:
![image](https://github.com/user-attachments/assets/565e4d3c-5922-437f-9b91-22fee217585c)

https://github.com/trgchinhh/DECC_Security/blob/main/TEST/Test_decode_DECC.py





