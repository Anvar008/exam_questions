from aiogram import Bot, filters, F, Dispatcher, types
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from pytube import YouTube
import ssl
from aiogram.types import FSInputFile

bot = Bot(token="7190554519:AAErPTeIhibFXPEEvC4mFefXroD1LEUStAQ")
dp = Dispatcher(bot=bot)


@dp.message(filters.Command("start"))
async def start_youtube_bot(message: types.Message):
    await message.answer("Добро пожаловать")


@dp.message()
async def downloadvideo_function(message: types.Message):
    url = YouTube(url=message.text)
    quality = url.streams.get_highest_resolution()
    download_video = quality.download()

    result = FSInputFile(download_video)
    await message.answer_video(video=result)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
