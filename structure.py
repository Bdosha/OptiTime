from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

main1: KeyboardButton = KeyboardButton(text='📆 Расписание')
main2: KeyboardButton = KeyboardButton(text='🎓 Курсы')
main3: KeyboardButton = KeyboardButton(text='👤 Профиль')
main4: KeyboardButton = KeyboardButton(text='❔ Помощь')

mainmenu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[main1, main2],
              [main3, main4]],
    resize_keyboard=True)

agree: KeyboardButton = KeyboardButton(text='✅ Подтвердить')
cansel: KeyboardButton = KeyboardButton(text='❌ Отмена')