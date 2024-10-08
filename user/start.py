import random

from aiogram import types
from dispatcher import dp, animation_url
from random_id import photo_id
from database import new_user, get_user_language
from keyboards import keyboard_language, tiktok_web
from load_language import load_language_files


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    languages = await load_language_files()

    lang = languages["lang"]
    strings_ru = languages["strings_ru"]
    strings_en = languages["strings_en"]
    strings_uk = languages["strings_uk"]
    strings_de = languages["strings_de"]
    strings_fr = languages["strings_fr"]
    strings_es = languages["strings_es"]
    strings_jap = languages["strings_jap"]
    strings_ko = languages["strings_ko"]
    strings_zh_hans = languages["strings_zh_hans"]
    strings_zh_hant = languages["strings_zh_hant"]

    await new_user(message.chat.id)
    user_id = message.from_user.id
    language = await get_user_language(user_id)

    if language is None:
        await message.answer_animation(animation_url, caption=lang["lang"], reply_markup=keyboard_language, parse_mode="HTML", protect_content=True)
    else:
        random_photo = random.choice(photo_id)
        if language == "ru":
            await message.answer_photo(random_photo, strings_ru["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "en":
            await message.answer_photo(random_photo, strings_en["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "uk":
            await message.answer_photo(random_photo, strings_uk["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "de":
            await message.answer_photo(random_photo, strings_de["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "fr":
            await message.answer_photo(random_photo, strings_fr["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "es":
            await message.answer_photo(random_photo, strings_es["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "jap":
            await message.answer_photo(random_photo, strings_jap["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "ko":
            await message.answer_photo(random_photo, strings_ko["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "zh_hans":
            await message.answer_photo(random_photo, strings_zh_hans["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
        elif language == "zh_hant":
            await message.answer_photo(random_photo, strings_zh_hant["start"], parse_mode="HTML", protect_content=True, reply_markup=tiktok_web)
