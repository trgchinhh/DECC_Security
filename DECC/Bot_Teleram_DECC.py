import telebot
from telebot import types
from DECC import *
import os, sys
from datetime import datetime
from lequangminh import * 

API_BOT = "THAY API BOT"
bot = telebot.TeleBot(API_BOT)

def banner():
    os.system("cls" if os.name == "nt" else "clear") # xoá tất cả những thứ còn lại trên terminal
    title = "\nHome: https://github.com/trgchinhh\n" 
    banner = """\n
██████╗░███████╗░█████╗░░█████╗░██████╗░███████╗   ███████╗███╗░░██╗░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝   ██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║█████╗░░██║░░╚═╝██║░░██║██║░░██║█████╗░░   █████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║░░██║██╔══╝░░██║░░██╗██║░░██║██║░░██║██╔══╝░░   ██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██╔══╝░░
██████╔╝███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗   ███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝███████╗
╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝   ╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚══════╝

        ░█████╗░██╗░░██╗██╗███╗░░██╗██╗░░██╗░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
        ██╔══██╗██║░░██║██║████╗░██║██║░░██║██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
        ██║░░╚═╝███████║██║██╔██╗██║███████║██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
        ██║░░██╗██╔══██║██║██║╚████║██╔══██║██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
        ╚█████╔╝██║░░██║██║██║░╚███║██║░░██║╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
        ░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
\n"""
    ban = Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_gray)), Center.XCenter(title)) + Colorate.Vertical(Colors.DynamicMIX((Col.light_red, Col.light_blue)), Center.XCenter(banner.center(300)))
    print(ban)

banner()    
tep_nguoi_dung = {}  # Lưu tạm thông tin file theo user

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>HÃY GỬI 1 FILE BẠN MUỐN MÃ HÓA CC HOẶC GIẢI MÃ</b>", parse_mode="HTML")


@bot.message_handler(content_types=['document'])
def handle_file(message):
    tai_lieu = message.document
    thong_tin_tep = bot.get_file(tai_lieu.file_id)
    duong_dan_tep = thong_tin_tep.file_path
    ten_tep = tai_lieu.file_name
    duoi_tep = os.path.splitext(ten_tep)[1]
    kich_thuoc_kb = round(tai_lieu.file_size / 1024, 2)
    thoi_gian_gui = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    id_tep = message.document.file_id
    id_tep_duy_nhat = message.document.file_unique_id
    loai_mime = message.document.mime_type

    du_lieu_tai_xuong = bot.download_file(duong_dan_tep)
    with open(f"./{ten_tep}", 'wb') as tep:
        tep.write(du_lieu_tai_xuong)

    with open(ten_tep, 'r', encoding='utf-8') as tep:
        noi_dung = tep.read()

    so_tu = len(noi_dung.split())
    so_ky_tu = sum(1 for ky_tu in noi_dung if ky_tu.isalpha())

    tep_nguoi_dung[message.chat.id] = {
        "ten_tep": ten_tep,
        "noi_dung": noi_dung
    }

    thong_tin = (
        f"<b>┌ Tên file:</b> {ten_tep}\n"
        f"<b>├ Định dạng:</b> {duoi_tep}\n"
        f"<b>├ Số từ:</b> {so_tu} từ\n"
        f"<b>├ Số ký tự:</b> {so_ky_tu} ký tự\n"
        f"<b>├ Dung lượng:</b> {kich_thuoc_kb} KB\n"
        f"<b>├ ID file:</b> {id_tep}\n"
        f"<b>├ ID file duy nhất:</b> {id_tep_duy_nhat}\n"
        f"<b>├ Loại mime:</b> {loai_mime}\n"
        f"<b>└ Gửi lúc:</b> {thoi_gian_gui}\n"
    )

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🔐 Encode", callback_data="encode"),
        types.InlineKeyboardButton("🔓 Decode", callback_data="decode")
    )

    bot.send_message(message.chat.id, thong_tin, parse_mode="HTML", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['encode', 'decode'])
def handle_action_selection(call):
    ma_nguoi_dung = call.message.chat.id
    hanh_dong = call.data

    if ma_nguoi_dung not in tep_nguoi_dung:
        bot.answer_callback_query(call.id, "❌ Không tìm thấy file")
        return

    tep_nguoi_dung[ma_nguoi_dung]["hanh_dong"] = hanh_dong
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🔑 Khóa 1", callback_data="key_1"),
        types.InlineKeyboardButton("🔑 Khóa 2", callback_data="key_2"),
        types.InlineKeyboardButton("🔑 Khóa 3", callback_data="key_3"),
        types.InlineKeyboardButton("🔑 Khóa 4", callback_data="key_4")
    )
    bot.edit_message_reply_markup(ma_nguoi_dung, call.message.message_id, reply_markup=None)
    bot.send_message(ma_nguoi_dung, "Vui lòng chọn 1 trong 4 khóa bên dưới", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith("key_"))
def handle_key_selection(call):
    ma_nguoi_dung = call.message.chat.id
    khoa = int(call.data.split("_")[1])

    if ma_nguoi_dung not in tep_nguoi_dung or "hanh_dong" not in tep_nguoi_dung[ma_nguoi_dung]:
        bot.answer_callback_query(call.id, "❌ Không thấy chọn khóa")
        return

    hanh_dong = tep_nguoi_dung[ma_nguoi_dung]["hanh_dong"]
    ten_tep = tep_nguoi_dung[ma_nguoi_dung]["ten_tep"]
    noi_dung = tep_nguoi_dung[ma_nguoi_dung]["noi_dung"]

    if hanh_dong == "encode":
        noi_dung_moi = ENCODE(noi_dung, khoa).encode()
        tep_moi = f"encoded_{ten_tep}"
        bot.answer_callback_query(call.id, f"✅ File hoàn thành mã hóa với {khoa}!")
    else:
        noi_dung_moi = DECODE(noi_dung, khoa).decode()
        tep_moi = f"decoded_{ten_tep}"
        bot.answer_callback_query(call.id, f"✅ File hoàn thành giải mã với {khoa}!")

    with open(tep_moi, "w", encoding="utf-8") as f:
        f.write(noi_dung_moi)

    with open(tep_moi, 'rb') as f:
        bot.send_document(ma_nguoi_dung, f, caption=f"📎 File {hanh_dong.upper()} với khóa {khoa} hoàn thành !")

    # os.remove(ten_tep)
    os.remove(tep_moi)
    del tep_nguoi_dung[ma_nguoi_dung]


if __name__ == "__main__":
    try:
        print("Bot đang khởi chạy !")
        bot.infinity_polling()
    except Exception as e:
        print(f"Lỗi : {e}")    
