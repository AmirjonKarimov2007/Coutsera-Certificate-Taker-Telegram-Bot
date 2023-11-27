from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
sertifikat = InlineKeyboardMarkup(row_width=1)
sertifikat.insert(InlineKeyboardButton(text="✅ Ha sertifikat olinsin",callback_data="sertifikat_yes"))
sertifikat.insert(InlineKeyboardButton(text="❌Yo'q seritikat olinmasin",callback_data="sertifikat_no"))

sertifikat_sender = InlineKeyboardMarkup(row_width=2)
sertifikat_sender.insert(InlineKeyboardButton(text="✅Sertikat yuborilsin",callback_data="sertifikat_sender_yes"))
sertifikat_sender.insert(InlineKeyboardButton(text="❌Sertikat yuborilmasin",callback_data="sertifikat_sender_no"))