import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

#переменная строковая, которая хранит token
# к телеграмм-боту
TOKEN = "8097881649:AAFqfnOzawLoA8rjM9A3IxyJuam3lAWHXXQ"
#dp - объект , Dispatcher() - вызов конструктора
dp = Dispatcher()

#Реакция на команду /start когда её ввел пользователь
#Кнопка Начать
#message - объект Message - тип_данных
#message.answer() - метод объекта message для отправки ответных
#сообщений
@dp.message(CommandStart())
async def command_start_handler(message:Message):
    await message.answer(f"Привет,{message.from_user.full_name}!")


#Бесконечный запуск бота
async def main()->None:
    #Создаем объект бота
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
