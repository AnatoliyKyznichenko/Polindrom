import os
##########
from aiogram import Bot, Dispatcher, executor, types
from tokens import *
from pytube import YouTube

# бот = сервер,который будет взаимодействовать с API Telegram.

bot = Bot(AUTH_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id,"Привет солнішко какое видео тебе скачать ^_^ ???\n"
                           "Отправь мне ссылку")

@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == "https://www.youtube.com/" or "youtube.com":
        await bot.send_message(chat_id,f"**Начинаю загрузку видео** : {yt.title}")

        await download_youtube_video(url,message,bot)


async def download_youtube_video(url,message,bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True,file_extension="mp4")
    stream.get_highest_resolution().download(f"{message.chat.id}",f"{message.chat.id}_{yt.title}")
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}","rb") as video:
        await bot.send_video(message.chat.id,video,caption="Вот твое видео ")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")





if __name__=="__main__":
    executor.start_polling(dp)