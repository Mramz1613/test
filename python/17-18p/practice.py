#
# summa = 0
# number = int(input("Введите число: "))
# minNum = number
# maxNum = number
# while number != 7:
#     summa += number
#     minNum = min(number,minNum)
#     maxNum = max(number,maxNum)
#     print(maxNum)
#     print(minNum)
#     print(summa)
#     number = int(input("Введите число: "))
# else: print("Good bye")
# count = 0
# for i in range(100,1000):
#     i = str(i)
#     if (i[0] == i[1]) or (i[1] == i[2]) or (i[0] == i[2]):
#         count +=1
# print(count)
# def math1(num1,num2):
#     return print(num1+num2)
#
#
# math1(1,1)
#
#
# def math2(num1,num2):
#     print("Функция math2 вызвана")
#     return (num1+num2)
#
# print(math2(3,4))

# l = int(input("Введите длину"))
# for i in range(l):
#     print("*"*l,end="")
#     print()

# #1 решение
# num1 = int(input("Введите размер стороны квадрата: "))
# symbol1 = str(input("Введите символ: "))
# for i in range(0,num1,1): #цикл отработает от 0 до введенного числа
#     print(num1*symbol1) # 3 * "+"   +++
#
# #1 решение 2ой вариант
# for i in range(0,num1,1):
#     print()
#     for j in range(0,num1,1):#
#         print(symbol1,end="")

# """Пользователь вводит с клавиатуры ширину и высоту прямоугольника.
# Требуется отобразить на экран заполненный прямоугольник с указанными высотой и шириной.
# Например, если пользователь ввёл высоту 3, а ширину 5 на экране будет выведено:
# *****
# *****
# *****
# Пользователь вводит с клавиатуры размер стороны квадрата.
# Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата). Размер стороны равен введённому размеру
# """

# w = int(input("Введите ширину "))
# l = int(input("Введите высоту "))
#
# for i in range(l):
#     print("*"*w)
# import  time
# side = int(input("Введите сторону квадрата "))
# for i in range(side):
#     for j in range(side):
#         if i == 0 or j == 0 or i == side-1 or j == side-1:
#             print("#",end="")
#         else:
#             print(" ",end="")
#     print("")
#     time.sleep(1)



# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for i in num:
#     print(i)
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, message
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties

Token = '7388377162:AAG9Ibum3LuvZ4a5twpX_WNo9fCWTqo6U4o'
dp = Dispatcher()
bot = Bot(token=Token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart()) # Отлов команды /Start
              # Мы пишем нашему боту
async def start(msg : Message): # сокращаем Message в msg
    button = [InlineKeyboardButton(text='Продолжить', callback_data='next')]
    send_button = InlineKeyboardMarkup(inline_keyboard=[button])
    await bot.send_message(chat_id=msg.chat.id,
                           text=f'да, {msg.from_user.first_name} это бот визитка',
                           reply_markup=send_button)



@dp.callback_query(F.data == 'next')
async def next(query : CallbackQuery):
    button = [InlineKeyboardButton(text = 'Контакты', callback_data= 'contacts'),
              InlineKeyboardButton(text= 'Услуги', callback_data='service')]
    send_button = InlineKeyboardMarkup(inline_keyboard=[button])
    await bot.send_photo(chat_id=query.message.chat.id, caption = 'бмв м5 кс левел',
                       photo= 'https://www.interfax.ru/ftproot/photos/photostory/2022/07/08/week/week5_1100.jpg',
                         reply_markup = send_button)














async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


































