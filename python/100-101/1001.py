import asyncio
import logging
import sys
from os import getenv
import random
import datetime as dt
import aiogram
from aiogram import F
from aiogram import Bot, Dispatcher, html, F,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,sticker
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder



TOKEN = "8097881649:AAFqfnOzawLoA8rjM9A3IxyJuam3lAWHXXQ"
dp = Dispatcher()

random_list = ["CAACAgIAAxkBAAEI40Jm_EpKkO3MWxAIFPCXVI1iTUGMOwACQFgAAsr0qEkDjuHgcnmwRjYE","CAACAgIAAxkBAAEI43xm_E19h9kFuHzTEpkDE3Ea-TvrqgACAgADFc2rFgwpvC0-k-V0NgQ","CAACAgIAAxkBAAEI435m_E1_Xl2udjGraZSgLGI_1MeeWgACAQADFc2rFlrnH0h0tnICNgQ"]

@dp.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(f"Привет,{message.from_user.full_name}")

@dp.message(Command("help"))
async def command_help(message: Message) -> None:
    await message.answer(f"Себе помоги,{message.from_user.full_name}")

@dp.message(Command("sticker"))
async def command_foto(message: Message) -> None:
    await message.answer_sticker(random.choice(random_list))

@dp.message(Command("foto"))
async def command_foto(message: Message) -> None:
    await message.answer_photo("https://masterpiecer-images.s3.yandex.net/c0c40f873f5811eeb12e6a2aaa288599:upscaled")

@dp.message(Command("sticker"))
async def command_foto(message: Message) -> None:
    await message.answer_sticker("CAACAgIAAxkBAAEI40Jm_EpKkO3MWxAIFPCXVI1iTUGMOwACQFgAAsr0qEkDjuHgcnmwRjYE")

@dp.message(F.sticker)
async def answer_stick(message: types.sticker):
    await message.answer_sticker("CAACAgIAAxkBAAEI40Jm_EpKkO3MWxAIFPCXVI1iTUGMOwACQFgAAsr0qEkDjuHgcnmwRjYE")

@dp.message(Command("dice"))
async def answer_dice(message: Message):
    await message.answer_dice(emoji="🎲")

@dp.message(Command("buttons"))
async def spec_butt(message:Message):
    builder = ReplyKeyboardBuilder()

    builder.row(
        types.KeyboardButton(text="Верхний ярус",request_location=True),
        types.KeyboardButton(text="Нижний ярус",request_contact=True)
    )

    builder.row(
        types.KeyboardButton(text="Сладкий домик", request_poll=types.KeyboardButtonPollType(type="quiz"))
    )

    await message.answer(
        "Куда нажать?", reply_markup=builder.as_markup(resize_keyboard = True)
    )

@dp.message(Command("line_menu"))
async def cmd_inline(message: Message, bot:Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Нижний ярус",url="https://optim.tildacdn.com/tild3437-3962-4865-a363-396164316639/-/contain/860x560/center/center/-/format/webp/2_1.jpg"),
                types.InlineKeyboardButton(text="Верхний ярус",url="https://optim.tildacdn.com/tild6539-6133-4363-a363-326239346565/-/contain/860x560/center/center/-/format/webp/1.jpg"),
                )
    builder.row(types.InlineKeyboardButton(text="Сладкий домик", url="https://static.tildacdn.com/tild6238-3764-4763-b562-336261656266/photo.jpg"))

    await message.answer(
        "Выберите ссылку",
        reply_markup=builder.as_markup()
    )

@dp.message(Command("contact"))
async def comand_contact(message: Message):
    await message.answer_contact("88005553535","Иван")

@dp.message(Command("time"))
async def comand_time(massage:Message):
    await massage.answer(f"Сейчас на моем компе {dt.datetime.now().hour} часов {dt.datetime.now().minute} минут")
#бесконечный запуск бота
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())