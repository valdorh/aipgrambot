from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMZZBwt-3VS0nRaB7VHJlbKuZBzNLAAAjgLAAJO5JlLMrFH0tlPjNAvBA')
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать в мой магазин!')


@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, я тебя не понял.')


if __name__ == '__main__':
    executor.start_polling(dp)
