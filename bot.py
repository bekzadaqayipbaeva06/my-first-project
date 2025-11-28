from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
import asyncio

TOKEN = ""
my_bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message):
    await message.answer("hi") 
    

async def main():
    print("I am starting ...")
    await dp.start_polling(my_bot)


#if __name__ == "__main__":
asyncio.run(main())
