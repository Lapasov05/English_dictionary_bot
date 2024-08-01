import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from Dispatcher import dp
from function import get_main_word, translate_text, translate_text_uz
import langid
from googletrans import Translator

translator = Translator()
load_dotenv()

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('BOT_TOKEN')



@dp.message(CommandStart())
async def Start(message: Message):
    username = message.from_user.first_name
    await message.answer(f"Hello {username}")
    await message.answer("Enter word:")


@dp.message()
async def tarjimon(message: types.Message):
    if len(message.text.split()) >= 2:
        text = translate_text(message.text)
        await message.reply(text)
    else:

        lookup = None

        word_id = message.text
        lookup = get_main_word(word_id)

        if lookup:
            await message.reply(f"Word {word_id}. \n Definitions: \n {lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            word_id = translate_text_uz(word_id)
            await message.reply(f"English translated word:\n👉  {word_id}")


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
