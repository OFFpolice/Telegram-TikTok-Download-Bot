from aiogram import types
from dispatcher import dp, admin_id
from database import get_user_language
from load_language import load_language_files


@dp.message_handler(commands=["admin"], user_id=admin_id)
async def admin_command(message: types.Message):
    languages = await load_language_files()

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

    user_id = message.from_user.id
    language = await get_user_language(user_id)
    messages = {
        "ru": strings_ru["admin"],
        "en": strings_en["admin"],
        "uk": strings_uk["admin"],
        "de": strings_de["admin"],
        "fr": strings_fr["admin"],
        "es": strings_es["admin"],
        "jap": strings_jap["admin"],
        "ko": strings_ko["admin"],
        "zh_hans": strings_zh_hans["admin"],
        "zh_hant": strings_zh_hant["admin"]
    }
    text_message = messages.get(language, "")
    await message.answer(text_message, parse_mode="HTML", protect_content=True)
