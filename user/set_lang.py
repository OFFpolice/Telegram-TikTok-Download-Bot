import random

from aiogram import types
from dispatcher import dp, bot
from database import set_user_language
from random_id import photo_id
from keyboards import tiktok_web
from load_language import load_language_files


@dp.callback_query_handler(lambda query: query.data in [
    "set_language_ru", "set_language_en", "set_language_uk", "set_language_de", 
    "set_language_fr", "set_language_es", "set_language_jap", "set_language_ko", 
    "set_language_zh_hans", "set_language_zh_hant"])
async def set_language(call: types.CallbackQuery):
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

    bot_info = await bot.get_me()
    bot_username = bot_info.username
    user_id = call.from_user.id

    if call.data == "set_language_ru":
        language = "ru"
        alert_message = strings_ru["alert_message"]
    elif call.data == "set_language_en":
        language = "en"
        alert_message = strings_en["alert_message"]
    elif call.data == "set_language_uk":
        language = "uk"
        alert_message = strings_uk["alert_message"]
    elif call.data == "set_language_de":
        language = "de"
        alert_message = strings_de["alert_message"]
    elif call.data == "set_language_fr":
        language = "fr"
        alert_message = strings_fr["alert_message"]
    elif call.data == "set_language_es":
        language = "es"
        alert_message = strings_es["alert_message"]
    elif call.data == "set_language_jap":
        language = "jap"
        alert_message = strings_jap["alert_message"]
    elif call.data == "set_language_ko":
        language = "ko"
        alert_message = strings_ko["alert_message"]
    elif call.data == "set_language_zh_hans":
        language = "zh_hans"
        alert_message = strings_zh_hans["alert_message"]
    elif call.data == "set_language_zh_hant":
        language = "zh_hant"
        alert_message = strings_zh_hant["alert_message"]

    await set_user_language(user_id, language)
    if language is None:
        await call.message.edit_text(lang["lang"], parse_mode="HTML")
    else:
        random_photo = random.choice(photo_id)
        caption = {
            "ru": strings_ru["start"],
            "en": strings_en["start"],
            "uk": strings_uk["start"],
            "de": strings_de["start"],
            "fr": strings_fr["start"],
            "es": strings_es["start"],
            "jap": strings_jap["start"],
            "ko": strings_ko["start"],
            "zh_hans": strings_zh_hans["start"],
            "zh_hant": strings_zh_hant["start"],
        }.get(language, "")
        caption = caption.format(bot_username=bot_username)
        await call.message.edit_media(
            media=types.InputMediaPhoto(media=random_photo, caption=caption, parse_mode="HTML"), 
            reply_markup=tiktok_web
        )
    await call.answer(text=alert_message, show_alert=False)
