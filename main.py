from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
from datetime import datetime

import config
import structure
import database

# импорт всех библиотек для работы

BOT_TOKEN: str = config.token

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    id = message.from_user.id
    print(message.from_user.username, message.from_user.id)
    if database.chek_user(id):
        await message.answer('Вы уже зарегистрированы', reply_markup=structure.mainmenu)
    else:
        await message.answer('Для начала работы с ботом, требуется пройти регистрацию',
                             reply_markup=ReplyKeyboardRemove())


@dp.message()
async def text_message(message: Message):  #
    print(message.from_user.username, message.text)
    id = message.from_user.id
    await message.answer(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)  # Запуск бота
