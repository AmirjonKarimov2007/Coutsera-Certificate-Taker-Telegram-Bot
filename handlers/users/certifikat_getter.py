import asyncio
from builtins import list
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from aiogram.dispatcher import FSMContext
import time
import re
import logging
import uuid
from keyboards.inline.sertikat_button import sertifikat
from keyboards.default.boglanish_button import boglanish
from app import on_startup
from data.config import ADMINS
from loader import dp
from loader import bot
from states.personalData import PersonalData
from aiogram.types import Message, CallbackQuery, ContentType
from keyboards.inline.sertikat_button import sertifikat_sender
import datetime
random_uuid = uuid.uuid4()
uuid_strings = str(random_uuid)
uuid_without_hyphens = uuid_strings.replace("-", "")



async def on_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await message.reply(f"Salom, {user_name}! Botimizga xush kelibsiz!")


async def wait_for_second_user(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await message.reply(f"Iltimos, {user_name}! Kutib turing, birinchi foydalanuvchi bilan bog'lanishni kuting.")


def gmail_generator():
    random_uuid = uuid.uuid4()
    uuid_strings = str(random_uuid)
    uuid_without_hyphens = uuid_strings.replace("-", "")
    return uuid_without_hyphens
#
# @dp.message_handler(text='🔖Sertifikat Olish', state=None)
# async def certificate(message: types.Message):
#     await message.reply("Iltimos Sertifikat uchun ism Familiyangizni yuboring!")
#     await PersonalData.fullName.set()
#
# @dp.message_handler(state=PersonalData.fullName)
# async def getter(message: types.Message, state: FSMContext):
#     name = message.text
#     contact_button = types.KeyboardButton("Share Contact", request_contact=True)
#     contact_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).insert(contact_button)
#     # Save the name in the FSMContext for later use
#     await state.update_data(
#         {"name": name}
#     )
#     await message.answer(f"Iltimos telefon raqamingizni yuboring:",reply_markup=contact_keyboard)
#     ism_familiya = name
#     await PersonalData.phoneNum.set()
# import re
# @dp.message_handler(content_types='contact',state=PersonalData.phoneNum)
# async def phone_num(message: types.Message,state: FSMContext):
#     data = await state.get_data()
#     name = data.get("name")
#     # Create a keyboard with the "Share Contact" button
#     phone_number = message.contact.phone_number
#     await state.update_data({"phone_number": phone_number})
#     await message.answer(f"Sizning ismingiz: {name}\n\n va shu nom ostida sertifikat oliniyapdi kutib turing:")
#
#     # Send a welcome message with the contact keyboard
#     await bot.send_message(chat_id=ADMINS[-1],text=f"Assalomu Aleykum Amirjon Yaxshimisiz?\n"
#                                                    f"Username: @{message.from_user.username} \nsizdan Sertifikat olmoqchi!\n"
#                                                    f"Sertifikat olmoqchi bo'lgan odamning Ismi:{name}\n\n"
#                                                    f"Telefon raqami: {phone_number}\n\n"
#                                                    f"Telegram Id:{message.from_user.id}",reply_markup=sertifikat)
#
# @dp.callback_query_handler(text="sertifikat_yes")
# async def start(call: types.CallbackQuery, state: FSMContext):
#     ism_pattern = r"Ismi:\s*([^\n]+)"
#     ism_match = re.search(ism_pattern, call.message.text)
#
#     id_pattern = r"Id:\s*([^\n]+)"
#     id_match = re.search(id_pattern, call.message.text)
#     user_id = id_match.group(1)
#
#     username_pattern = r"Username:\s*([^\n]+)"
#     username_match = re.search(username_pattern, call.message.text)
#     username = username_match.group(1)
#
#     phone_pattern = r"raqami:\s*([^\n]+)"
#     phone_match = re.search(phone_pattern, call.message.text)
#     phone_number = phone_match.group(1)
#
#     if user_id:
#         logging.info(user_id)
#         data = await state.get_data()
#         ism_familiya = ism_match.group(1)
#         print(ism_familiya)
#         await state.update_data({"id": user_id})
#         await state.update_data({"phone_number": phone_number})
#         await state.update_data({"username": username})
#         options = webdriver.ChromeOptions()
#         options.add_extension("/home/amirjon/Desktop/course_cert_using_selenium/NopeCHA-CAPTCHA-Solver.crx")
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         name = ism_familiya
#         await state.update_data({"name": name})
#         email = gmail_generator() + '@gmail.com'
#         password = "aslkjfhladskjhfkajsdhflkasjd44hfkajsdhfskjdhf"
#
#         # Your other logic here
#         # <<<<<<<<<<<<<<start getting>>>>>>>>>>>>>>
#         driver = webdriver.Chrome(options=options)
#         await state.update_data({"id": user_id})
#
#         link = await get_certificate(driver, name, email, password)
#         await asyncio.sleep(2)
#         await state.update_data({"link": link})
#
#         try:
#             await call.message.edit_reply_markup()
#             await call.message.delete()
#             await call.message.answer(f"{name}, seritifikat tayyor ✅\n{link}", reply_markup=sertifikat_sender)
#             await asyncio.sleep(3)
#             await PersonalData.sertifikat.set()
#
#         except:
#             await call.message.answer(f"{name} sertifikat tayyorlashda muammo yuz berdi ❌")
#             await bot.send_message(chat_id=ADMINS[-1],
#                                    text=f"{name},da sertifikat olishda muammo bo'ldi:{call.from_user.username}")
#         driver.close()
#     else:
#         logging.warning("user_id is None or invalid")
#
# @dp.callback_query_handler(text="sertifikat_sender_yes",state=PersonalData.sertifikat)
# async def yes_or_no(call: types.CallbackQuery,state: FSMContext):
#     await call.message.edit_reply_markup()
#     await call.message.delete()
#     data = await state.get_data()
#     user_id = data.get("id")
#     name = data.get("name")
#     link = data.get("link")
#     username = data.get("username")
#     phone_number = data.get("phone_number")
#     await call.message.answer(f"▪️Ism Famliya:<b>{name}</b>\n\n"
#                               f"🔗Sertifikat linki:<b>{link}</b>\n\n"
#                               f"👤Telegram foydalanuvchi: <b>{username}</b>\n\n"
#                               f"📞Telefon raqami: {phone_number}\n\n"
#                               f"🆔Foydalanuvchi id: {user_id}\n\n\n"
#                               f"<b>✅Sertifikat Muvaffaqiyatli Taqdim etildi</b>")
#     await bot.send_message(chat_id=user_id, text=f"{name},Nomi ostidagi sertifikat tayyor ✅\n\n{link}")
#     await state.finish()
# ...
@dp.message_handler(text='🔖Sertifikat Olish',state=None)
async def get_fullname(message: types.Message, state: FSMContext):
    await message.reply("Ilimos ismingizni kiriting va shu nom ostida sertifikat olinadi!")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.fullName)
async def process_full_name(message: types.Message, state: FSMContext):
    # Assuming the user's full name is provided in the message text
    full_name = message.text

    # Save the full name in the state
    await state.update_data(full_name=full_name)
    contact_button = types.KeyboardButton("Share Contact", request_contact=True)
    contact_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).insert(contact_button)
    # Move to the next state
    await state.update_data(message_id=message.message_id)
    await PersonalData.next()
    await message.reply("Yaxshi, hozir telefon raqamingizni yuboring!",reply_markup=contact_keyboard)
@dp.message_handler(content_types='contact',state=PersonalData.phoneNum)
async def process_phone_number(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    message_id = user_data.get('message_id')
    # Assuming the user's phone number is provided in the message text
    phone_number = message.contact.phone_number
    username= message.from_user.username
    user_id = message.from_user.id
    await state.update_data(phone_number=phone_number)
    await state.update_data(username = username)
    await state.update_data(user_id = user_id)
    user_data = await state.get_data()
    fullname = user_data['full_name']
    phone_number = user_data['phone_number']
    user_id = user_data['user_id']
    # Save the phone number in the state
    await message.reply("Iltimos Kuting! Sizning Sertifikat olish buyicha arizangiz ko'rib chiqiliyapdi agar admin ruxsat bersa sizga sertifikat olinadi!")
    xabar = await bot.send_message(chat_id=ADMINS[-1], text=f"Assalomu Aleykum Amirjon Yaxshimisiz?\n"
                                                       f"Username: @{username} \nsizdan Sertifikat olmoqchi!\n"
                                                       f"Sertifikat olmoqchi bo'lgan odamning Ismi:{fullname}\n\n"
                                                       f"Telefon raqami: {phone_number}\n\n"
                                                       f"Telegram Id:{user_id}",reply_markup=sertifikat)
    await asyncio.sleep(2)
    await bot.pin_chat_message(chat_id=ADMINS[-1], message_id=xabar.message_id)
    await state.finish()
@dp.message_handler(content_types=ContentType.PINNED_MESSAGE)
async def delete_pin_notification(message: types.Message):
    await message.delete()
@dp.callback_query_handler(text="sertifikat_yes")
async def process_certificate_sender(call: types.CallbackQuery, state: FSMContext):
    # Assuming the certificate sender information is provided in the message text
    # user_data = await state.get_data()
    # ism_familiya = user_data['full_name']
    # phone_number = user_data['phone_number']
    # user_id = user_data['user_id']
    # username = user_data['username']
    message_text = call.message.text

    id_pattern = r"Id:\s*([^\n]+)"
    id_match = re.search(id_pattern, message_text)
    user_id = id_match.group(1)

    ism_pattern = r"Ismi:\s*([^\n]+)"
    ism_match = re.search(ism_pattern, message_text)
    ism_familiya = ism_match.group(1)


    username_pattern = r"Username:\s*([^\n]+)"
    username_match = re.search(username_pattern, message_text)
    username = username_match.group(1)

    phone_pattern = r"raqami:\s*([^\n]+)"
    phone_match = re.search(phone_pattern, message_text)
    phone_number = phone_match.group(1)


    if user_id:
        logging.info(user_id)
        print(ism_familiya)
        options = webdriver.ChromeOptions()
        options.add_extension("/home/amirjon/Desktop/course_cert_using_selenium/NopeCHA-CAPTCHA-Solver.crx")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        name = ism_familiya
        email = gmail_generator() + '@gmail.com'
        password = "aslkjfhladskjhfkajsdhflkasjd44hfkajsdhfskjdhf"

        # Your other logic here
        # <<<<<<<<<<<<<<start getting>>>>>>>>>>>>>>
        driver = webdriver.Chrome(options=options)

        link = await get_certificate(driver, name, email, password)
        await asyncio.sleep(2)

        try:
            await call.message.edit_reply_markup()
            await call.message.delete()
            await call.message.answer(f"Assalomu Aleykum Amirjon\n"
                                                       f"Username: @{username} \n\n"
                                                       f"Link:{link}\n\n"
                                                       f"Sertifikat olmoqchi bo'lgan odamning Ismi:{ism_familiya}\n\n"
                                                       f"Telefon raqami: {phone_number}\n\n"
                                                       f"Telegram Id:{user_id}",reply_markup=sertifikat_sender)
            await asyncio.sleep(3)


        except:
            await call.message.answer(f"{name} sertifikat tayyorlashda muammo yuz berdi ❌",reply_markup=boglanish)
            await bot.send_message(chat_id=ADMINS[-1],
                                   text=f"{name},da sertifikat olishda muammo bo'ldi:{call.from_user.username}")
        driver.close()
    else:
        logging.warning("user_id is None or invalid")
    # Optionally, you can reset the state

    # Process the collected data as needed
    # await message.reply(f"Ma'lumotlar saqlandi: {user_data['user_id']}")

@dp.callback_query_handler(text='sertifikat_sender_yes')
async def process_certificate_sender(call: types.CallbackQuery, state: FSMContext):

    message_text = call.message.text
    print(message_text)
    id_pattern = r"Id:\s*([^\n]+)"
    id_match = re.search(id_pattern, message_text)
    user_id = id_match.group(1)
    link_pattern = r"Link:\s*([^\n]+)"
    link_match = re.search(link_pattern, message_text)
    link = link_match.group(1)
    ism_pattern = r"Ismi:\s*([^\n]+)"
    ism_match = re.search(ism_pattern, message_text)
    ism_familiya = ism_match.group(1)

    username_pattern = r"Username:\s*([^\n]+)"
    username_match = re.search(username_pattern, message_text)
    username = username_match.group(1)

    phone_pattern = r"raqami:\s*([^\n]+)"
    phone_match = re.search(phone_pattern, message_text)
    phone_number = phone_match.group(1)



    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer(f"▪️Ism Famliya:<b>{ism_familiya}</b>\n\n"
                              f"🔗Sertifikat linki:<b>{link}</b>\n\n"
                              f"👤Telegram foydalanuvchi: <b>{username}</b>\n\n"
                              f"📞Telefon raqami: {phone_number}\n\n"
                              f"🆔Foydalanuvchi id: {user_id}\n\n\n"
                              f"<b>✅Sertifikat Muvaffaqiyatli Taqdim etildi</b>")
    await bot.send_message(chat_id=user_id,text=f"{ism_familiya},Nomi ostidagi sertifikat tayyor ✅\n\n{link}\n\n\n\n🤝Qo'llab quvvatlash uchun\n\nAmirjon Karimov\n👉9760080151866938",reply_markup=boglanish)
    CHANNEL_ID = '@Uzbekcoders_uz_sertifikatlar'
    await bot.send_message(chat_id=CHANNEL_ID, text=f"▪️Ism Famliya:<b>{ism_familiya}</b>\n\n"
                              f"🔗Sertifikat linki:<b>{link}</b>\n\n"
                              f"🆔Foydalanuvchi id: {user_id}\n\n\n"
                              f"<b>✅Sertifikat Muvaffaqiyatli Taqdim etildi</b>")


async def get_certificate(driver, name, email, password):
    await enroll(driver, name, email, password)
    await resume_assignment(driver)
    await test_assignment(driver)
    await name_verification(driver, name)
    link = await download(driver)
    driver.get(link)
    # await cleanup()
    return link


async def sign_in(driver, fullname, email, password):
    driver.get("https://www.coursera.org/projects/youtube-small-business-marketing?action=enroll&authMode=signup")
    print('boshlandi')
    await asyncio.sleep(5)
    # Use WebDriverWait to wait for the name input field to be present
    try:
        login = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "name"))
            or EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[7]/div/div/section/section/div[1]/form/button"))
            # Use a different locator if necessary
        )
        login.send_keys(fullname)
        print('login kiritildi')
    except:
        print('login kirirish amalga oshmadi')
    try:
        # Find and fill the email input field
        email_name = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, 'email'))
            or EC.presence_of_element_located((By.ID, 'email'))  # Use a different locator if necessary
        )
        email_name.send_keys(email)
        print("email kiritildi")
    except:
        print('email kiritish amailga oshmadi')

    try:

        # Find and fill the password input field
        password_name = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, 'password'))
            or EC.presence_of_element_located((By.ID, 'password'))  # Use a different locator if necessary
        )
        password_name.send_keys(password)
        print("parol muvaffaqiyatli kiritildi!")
        await asyncio.sleep(1)
    except:
        print("parol kiritish amalga oshmadi!")
    # Find and click the login button
    try:
        login_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CLASS_NAME, '_6dgzsvq.css-j6v0dd')))

        login_btn.click()
        print("submitni bosish muvaffaqiyatli amalga oshdi")
    except:
        login_btn = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/section/section/div[1]/form/button'))
            or EC.element_to_be_clickable((By.ID, 'loginButton'))
        )
        login_btn.click()
        print('submit bosilmadi')
    try:
        WebDriverWait(driver, 60).until(
            EC.url_to_be('https://www.coursera.org/projects/youtube-small-business-marketing?action=enroll')
        )
        # Wait for the page to load after clicking the login button
        await asyncio.sleep(10)  # You might need to adjust this based on your application
        print("login sahifasi toliq baarildi")
    except:
        print("login sahifasidan o'tolmadik!")
async def enroll(driver, name, email, password):
    logging.info('<------------------Dastur ishga Tushdi------------------>')
    await sign_in(driver, name, email, password)

    # Replace with your actual email and password
    driver.get('https://www.coursera.org/projects/youtube-small-business-marketing')
    await asyncio.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "c-modal-overlay"))
    )

    enroll_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cds-button-primary"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", enroll_button)
    await asyncio.sleep(1)
    driver.execute_script("arguments[0].click();", enroll_button)
    await asyncio.sleep(5)

    # Check if the "primary.cozy.continue-button" is present and clickable
    try:
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "primary.cozy.continue-button"))
        )
        await asyncio.sleep(1)
        continue_button.click()
        await asyncio.sleep(3)
    except:
        pass
async def resume_assignment(driver):
    try:
        driver.get(
            'https://www.coursera.org/learn/youtube-small-business-marketing/exam/fEJPQ/graded-quiz-test-your-project-understanding/attempt')
        await asyncio.sleep(4)
        resume_btn = driver.find_element(By.CLASS_NAME,
                                         "cds-105.cds-button-disableElevation.cds-button-primary.css-k93wf6")

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView(true);", resume_btn)
        await asyncio.sleep(1)

        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", resume_btn)
        await asyncio.sleep(3)
        close_btn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div/div[2]/div[3]/div/button"))
        )
        # close_btn= driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div/div[2]/div[3]/div/button')
        close_btn.click()
        await asyncio.sleep(3)
        print('passet')

    except:
        resume_btn = driver.find_element(By.CLASS_NAME,
                                         "cds-105.cds-button-disableElevation.cds-button-primary.css-k93wf6")

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView(true);", resume_btn)
        await asyncio.sleep(1)

        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", resume_btn)
        await asyncio.sleep(3)
        close_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div/div/div[1]/button"))
        )
        close_button.click()
        # close_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div[1]/button')
        # close_btn.click()
        await asyncio.sleep(3)
        print('failed')
async def test_assignment(driver):
    await asyncio.sleep(3)

    try:
        # Test Question 1
        test_one = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Yes, there is!')]"))
        )
        test_one.click()
        await asyncio.sleep(0.5)

        # Test Question 2
        test_two = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'False')]"))
        )
        test_two.click()
        await asyncio.sleep(0.5)

        # Test Question 3
        test_three = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'There is no limit to the amount of videos you can ')]"))
        )
        test_three.click()
        await asyncio.sleep(0.5)

        # Test Question 4
        test_four = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Yes, they can.')]"))
        )
        test_four.click()
        await asyncio.sleep(0.5)

        # Agree to terms
        agree = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cds-checkboxAndRadio-label"))
        )
        agree.click()

        await asyncio.sleep(2)

        # Input legal name
        inputing = driver.find_element(By.XPATH, "//input[@placeholder='Enter your legal name']")
        inputing.send_keys('salom')

        # Submit the test
        try:
            submit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Submit']"))
            )
            submit.click()
        except:
            submit = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div[6]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/button[1]"))
            )
            submit.click()

    except Exception as e:
        print(f"Error during test_assignment: {e}")
async def name_verification(driver, name):
    await asyncio.sleep(2)
    driver.get('https://www.coursera.org/user-verification')

    await asyncio.sleep(3)
    try:
        await asyncio.sleep(2)
        # Firstname
        first_name = driver.find_element(By.XPATH, "html/body/div[2]/div/div/div/div[1]/div[1]/div/div/input")
        first_name.send_keys(name)

        await asyncio.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/label/div/span")
        await asyncio.sleep(1)
        checkbox.click()
        await asyncio.sleep(3)
        try:
            submit = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[3]/button")
            await asyncio.sleep(1)
            submit.click()
            await asyncio.sleep(3)
        except:
            versub = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button")))
            versub.click()
            print('versub error')

    except:
        print('Name verificationda error bor')
async def download(driver):
    driver.get('https://www.coursera.org/learn/youtube-small-business-marketing/home/week/1')
    await asyncio.sleep(5)
    href = driver.find_element(By.XPATH,
                               '//*[@id="main"]/div/div/div/div/div/div/div[2]/div[3]/div/div[1]/div[2]/div[2]/a')
    hreff = href.get_attribute('href')
    print("href", hreff)
    return hreff


# async def cleanup():
#     # Close the browser
#     driver.save_screenshot('rasmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm.png')
#     await asyncio.sleep(10)
#     driver.quit()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(on_startup(dp))
    loop.create_task(executor.start_polling(dp, on_startup=on_startup))
    loop.run_forever()
