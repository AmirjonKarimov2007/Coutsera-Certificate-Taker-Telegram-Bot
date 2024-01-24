import io
from loader import dp, db, bot
from aiogram import types
import asyncpg
from data.config import ADMINS
from utils.db_api import db_commands
from aiogram.types import ParseMode
from aiogram.types.web_app_info import WebAppInfo
@dp.message_handler(commands=['users'],user_id=ADMINS)
async def send_table(message: types.Message):
    users_data = await db.select_all_users()
    for user in users_data:
        fullname = user.get('full_name')
        username = user.get('username')
        telegram_id = user.get('telegram_id')
        try:
            name = await db.add_user(
                full_name=fullname,
                username=username,
                telegram_id=telegram_id,
                )
        except asyncpg.exceptions.UniqueViolationError:
            name = await db.select_user(telegram_id=telegram_id)

@dp.message_handler(commands=['screenshot'],user_id=ADMINS)
async def send_screenshot(message: types.Message):
    # Capture the screenshot

    # Save the screenshot to a BytesIO object
    image_bytes = io.BytesIO()
    screenshot.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Send the screenshot as a photo
    await bot.send_photo(message.chat.id, photo=image_bytes)
@dp.message_handler(commands='reklama',user_id=ADMINS)
async def reklama(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        text = f"Assalomu Aleykum Xurmatli foydalanuvchilar sizlarga bizning yangi telegram botimizni taqdim qilmoqchimiz.\n" \
               f"Umid qilamizki siz u botdan kerakli maqsadlarda foydalanasiz!\n" \
               f"Qo'llab quvvatlash uchun:\n" \
               f"9860070151866938"
        await bot.send_message(user['telegram_id'],text)
@dp.message_handler(commands='remove_user')
async def remove_user(message: types.Message):
    rm_user = await db.delete_user(5816753017)
    await message.answer('foydalanuvchi ochirildi')
