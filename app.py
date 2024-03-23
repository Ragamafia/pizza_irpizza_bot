import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


bot = Bot(token='6996415512:AAFNgePCqxbPKFD4qoSBtTHpaqoopmkolWg')

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Была команда Старт')


@dp.message()
async def echo(message: types.Message) -> None:
    text: str | None = message.text

    if text in ['привет', 'Привет', 'hi', 'hello']:
        await message.answer('И тебе привет!')
    elif text in ['пока', 'Пока', 'by']:
        await message.answer('И тебе пока!')
    else:
        await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())