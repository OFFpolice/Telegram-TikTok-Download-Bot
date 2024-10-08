from aiogram import types
from dispatcher import dp, animation_url
from keyboards import keyboard_language
from load_language import load_language_files


@dp.message_handler(commands=["lang"])
async def lang_command(message: types.Message):
    languages = await load_language_files()
    lang = languages["lang"]

    await message.answer_animation(
        animation_url,
        caption=lang["lang"],
        reply_markup=keyboard_language,
        parse_mode="HTML",
        protect_content=True
    )
