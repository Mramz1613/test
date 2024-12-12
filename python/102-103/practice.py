import asyncio
import logging
import sys
import random
import datetime as dt
from aiogram import Bot, Dispatcher, html, F, types
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,sticker
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder




TOKEN = "8097881649:AAFqfnOzawLoA8rjM9A3IxyJuam3lAWHXXQ"
dp = Dispatcher()

random_list = ["CAACAgIAAxkBAAEI40Jm_EpKkO3MWxAIFPCXVI1iTUGMOwACQFgAAsr0qEkDjuHgcnmwRjYE","CAACAgIAAxkBAAEI43xm_E19h9kFuHzTEpkDE3Ea-TvrqgACAgADFc2rFgwpvC0-k-V0NgQ","CAACAgIAAxkBAAEI435m_E1_Xl2udjGraZSgLGI_1MeeWgACAQADFc2rFlrnH0h0tnICNgQ"]

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


@dp.message(CommandStart())
async def spec_butt(message:Message):
    builder =[[
        types.KeyboardButton(text="ВК"),
        types.KeyboardButton(text="Instagram"),
        types.KeyboardButton(text="Сайт")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=builder,resize_keyboard=True)
    await message.answer("Выберите соц сеть",reply_markup=keyboard)

@dp.message(F.text.lower() == "вк")
async def vk(message:Message):
    await message.answer("https://vk.com/gnezdo_39")

@dp.message(F.text.lower() == "instagram")
async def inst(message:Message):
    await message.answer("https://www.instagram.com/gnezdo_kld/")

@dp.message(F.text.lower() == "сайт")
async def site(message:Message):
    await message.answer("t.me/gnezdo_new_bot/kode")


@dp.message(Command("line_menu"))
async def cmd_inline(message: Message, bot:Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Нижний ярус",url="https://optim.tildacdn.com/tild3437-3962-4865-a363-396164316639/-/contain/860x560/center/center/-/format/webp/2_1.jpg"),                types.InlineKeyboardButton(text="Верхний ярус",url="https://optim.tildacdn.com/tild6539-6133-4363-a363-326239346565/-/contain/860x560/center/center/-/format/webp/1.jpg"),                )
    builder.row(types.InlineKeyboardButton(text="Сладкий домик", url="https://static.tildacdn.com/tild6238-3764-4763-b562-336261656266/photo.jpg"))

    await message.answer(
        "Выберите ссылку",        reply_markup=builder.as_markup()
    )

@dp.message(Command("contact"))
async def comand_contact(message: Message):
    await message.answer_contact("88005553535","Иван")

@dp.message(Command("time"))
async def comand_time(massage:Message):
    await massage.answer(f"Сейчас на моем компе {dt.datetime.now().hour} часов {dt.datetime.now().minute} минут")
@dp.message(Command("random"))
async def comnand_random(message:Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми",
        callback_data="random_value"))
    await message.answer("Нажмите кнопку чтобы бот отправил от 1 до 10",
                         reply_markup=builder.as_markup()
                         )
@dp.callback_query(F.data=="random_value")
async def send_random_value(callback:types.CallbackQuery):
    await callback.message.answer(str(random.randint(1,10)))
    await callback.answer("Спс")
user_data = {}
def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="+1",callback_data="num_up"),
            types.InlineKeyboardButton(text="-1", callback_data="num_dw")
        ],[types.InlineKeyboardButton(text="Подтвердить",callback_data="num_end")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

async def update_num_text(message: types.Message,new_value:int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard()
        )


@dp.message(Command("numbers"))
async def cmd_nums(message:types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0",reply_markup=get_keyboard())


@dp.callback_query(F.data.startswith("num_"))
async def call_back_nums(callback:types.CallbackQuery):
    user_value = user_data.get(callback.from_user.id,0)
    action = callback.data.split("_")[1]
    if action == "up":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message,user_value+1)
    elif action == "dw":
        user_data[callback.from_user.id] = user_value - 1
        await update_num_text(callback.message, user_value - 1)
    elif action == "end":
        await callback.message.edit_text(f"Итого: {user_value}")

def menu_buttons():
    buttons = [[types.InlineKeyboardButton(text="Верхний ярус",callback_data="gnezdo_up")],
               [types.InlineKeyboardButton(text="Нижний ярус",callback_data="gnezdo_down")],
               [types.InlineKeyboardButton(text="Сладкий домик",callback_data="gnezdo_sweet")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def first_menu():
    buttons = [
                [
                types.InlineKeyboardButton(text="Рыба на гриле",callback_data="first_fish"),
                types.InlineKeyboardButton(text="Мясо на гриле",callback_data="first_meat")
                ],
               [
                   types.InlineKeyboardButton(text="Кесадилья",callback_data="first_kesa"),
                   types.InlineKeyboardButton(text="Гарниры", callback_data="first_garnish"),
                   types.InlineKeyboardButton(text="Супы", callback_data="first_soup")
                ],
                [
                    types.InlineKeyboardButton(text="Фрай", callback_data="first_fry"),
                    types.InlineKeyboardButton(text="Чай/Кофе", callback_data="first_tea"),
                    types.InlineKeyboardButton(text="Горячие напитки", callback_data="first_hotdrink")
               ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data="first_back"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def second_menu():
    buttons = [
        [types.InlineKeyboardButton(text="Бургеры и буррито",callback_data="second_burger"),
         types.InlineKeyboardButton(text="Поке/Боулы",callback_data="second_poke")
         ],
        [types.InlineKeyboardButton(text="Балтийская кухня",callback_data="second_balt"),
         types.InlineKeyboardButton(text="Супы",callback_data="second_soup"),
         types.InlineKeyboardButton(text="Фрайз",callback_data="second_fry")
         ],
        [types.InlineKeyboardButton(text="Десерты",callback_data="second_desert"),
         types.InlineKeyboardButton(text="Чай/Кофе",callback_data="second_tea"),
         types.InlineKeyboardButton(text="Горячие напитки",callback_data="second_hotdrinks")
         ],
        [types.InlineKeyboardButton(text="Назад",callback_data="second_back")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def sweet_menu():
    buttons = [
    [types.InlineKeyboardButton(text="Тредельник",callback_data="sweet_trdel"),
     types.InlineKeyboardButton(text="Пян-се",callback_data="sweet_pyanse"),
     types.InlineKeyboardButton(text="Чуррос",callback_data="sweet_chur")
    ],
    [
    types.InlineKeyboardButton(text="Кофе",callback_data="sweet_coffee"),
    types.InlineKeyboardButton(text="Чай",callback_data="sweet_tea"),
    types.InlineKeyboardButton(text="Молочный коктейль",callback_data="sweet_milk")
    ],
    [types.InlineKeyboardButton(text="Назад",callback_data="sweet_back")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

@dp.message(Command("menu"))
async def show_menu(message:Message):
    await message.answer("Выберите меню", reply_markup=menu_buttons())

@dp.callback_query(F.data.startswith("gnezdo_"))
async def call_back_menu(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    if action == "up":
        await callback.message.edit_text("Вы выбрали нижний этаж",reply_markup=first_menu())
    elif action == "down":
        await callback.message.edit_text("Вы выбрали верхний этаж",reply_markup=second_menu())
    elif action == "sweet":
        await callback.message.edit_text("Вы выбрали сладкий домик",reply_markup=sweet_menu())


@dp.callback_query(F.data.startswith("first_"))
async def call_back_first(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    if action == "up":
        await callback.message.edit_text("Вы выбрали верхний этаж")
    elif action == "down":
        await callback.message.edit_text("Вы выбрали нижний этаж")
    elif action == "sweet":
        await callback.message.edit_text("Вы выбрали сладкий домик")
    elif action == "back":
        await callback.message.edit_text("Выберите меню",reply_markup=menu_buttons())

@dp.callback_query(F.data.startswith("second_"))
async def call_back_first(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    if action == "back":
        await callback.message.edit_text("Выберите меню",reply_markup=menu_buttons())


@dp.callback_query(F.data.startswith("sweet_"))
async def call_back_first(callback:types.CallbackQuery):
    action = callback.data.split("_")[1]
    if action == "back":
        await callback.message.edit_text("Выберите меню",reply_markup=menu_buttons())
#бесконечный запуск ботаasync def main() -> None:
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())