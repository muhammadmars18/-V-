import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message,FSInputFile, KeyboardButton, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


TOKEN = "6040556971:AAE7Z4DuV5swg9CPrGlNltrUeXbkZtVZv_k"
dp = Dispatcher()
ADMIN = 6084834749  

class support(StatesGroup):
    Ism = State()
    Telefon = State()


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

tugmalar = ReplyKeyboardBuilder(
    markup=[
        [KeyboardButton(text='Bir') , KeyboardButton(text='Ikki')],
        [KeyboardButton(text='Uch') ]
    ]
)


class Confirming(StatesGroup):
    confirming = State()


inline_menu = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text='Rasm', callback_data='rasm'),
         InlineKeyboardButton(text='Video', callback_data='video')],
        [InlineKeyboardButton(text='Gif', callback_data='gif')],
        [InlineKeyboardButton(text='Audio', callback_data='audio')]

    ]
)



@dp.callback_query(F.data == 'rasm')
async def send_photo(call: CallbackQuery):
    await call.message.answer_photo("https://media.gettyimages.com/id/2155052917/photo/borussia-dortmund-v-real-madrid-cf-uefa-champions-league-final-2023-24.jpg?s=1024x1024&w=gi&k=20&c=gwOkfakAzd9OSel5dR-rktNI-GhjHIvjVnbMtr33bgE=")


    


@dp.callback_query(F.data == 'gif')
async def send_animation(call: CallbackQuery):
    await call.message.answer_animation("https://compote.slate.com/images/697b023b-64a5-49a0-8059-27b963453fb1.gif")

@dp.callback_query(F.data == 'video')
async def send_animation(call: CallbackQuery):
    # video_file = FSInputFile(path='video/mega.mp4')
    await call.message.answer_animation('https://videos.pexels.com/video-files/2099568/2099568-sd_640_360_30fps.mp4')

@dp.callback_query(F.data == 'audio')
async def send_animation(call: CallbackQuery):
    # audio_file = FSInputFile(path='video/real.mp')
    await call.message.answer_animation('https://videos.pexels.com/video-files/856148/856148-sd_640_360_25fps.mp4')

@dp.message(Command(commands=['support']))
async def command_help_hangler(nimadur: Message, state:FSMContext):
    await nimadur.answer('<a> Ismingizni va telefon raqamingizni kiriting!!!</a>')

@dp.callback_query(F.data == 'correct', Confirming.confirming)
async def correct_callback_query_handler(telefon: CallbackQuery, state: FSMContext, nimadur: Message):
    data = await state.get_data()
    matn = data.get('text')
    await bot.send_message(
        chat_id=ADMIN,
        text=matn,
        reply_markup=inline_menu.as_markup()
    )
    await nimadur.answer('xabaringiz adminga yuborildi! :)'),

#     await state.clear()
#     await telefon.message.delete()

@dp.message(F.text == 'Bir')
async def xabar_handler(xabar:Message, state: FSMContext):
    await xabar.answer(text="Bir",
                       reply_markup=inline_menu.as_markup()
                       )
    
@dp.message(F.text == 'Ikki')
async def xabar_handler(xabar:Message, state: FSMContext):
    await xabar.answer(text="Ikki",
                       reply_markup=inline_menu.as_markup()
                       )

@dp.message(F.text == 'Uch')
async def xabar_handler(xabar:Message, state: FSMContext):
    await xabar.answer(text="Uch",
                       reply_markup=inline_menu.as_markup()
                       )



@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Salom {html.bold(message.from_user.full_name)}! mening ismim Back Men sizga rasm, audio, Gif va vidio Tashlab beradigan botman", reply_markup= tugmalar.as_markup(resize_keyboard=True))


@dp.message(Command(commands=['help']))
async def command_help_handler(nimadur: Message):
    await nimadur.answer('<i> Men sizga qanday yordam bera olaman, shuni menga chunarli qilib yozsangiz men sizga yordam beraman,o\'zi muammo nima?</i>')

@dp.message(Command(commands=['support']))
async def command_help_handler(nimadur: Message):
    await nimadur.answer('Salom👋!')




async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())