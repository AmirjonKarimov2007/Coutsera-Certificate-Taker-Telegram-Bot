from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    sertificat_chek = State()
    fullName = State() # ism
    phoneNum = State() # Tel raqami
    # sertifikat_sender = State() #sertifikat oladi
