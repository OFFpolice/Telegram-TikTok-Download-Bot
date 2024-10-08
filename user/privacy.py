from aiogram import types
from dispatcher import dp, bot
from database import get_user_language
from load_language import load_language_files


@dp.message_handler(commands=["privacy"])
async def privacy_command(message: types.Message):
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
    bot_info = await bot.get_me()
    bot_username = bot_info.username

    if language == "ru":
        privacy_message = strings_ru["privacy_message"]
    elif language == "en":
        privacy_message = strings_en["privacy_message"]
    elif language == "uk":
        privacy_message = strings_uk["privacy_message"]
    elif language == "de":
        privacy_message = strings_de["privacy_message"]
    elif language == "fr":
        privacy_message = strings_fr["privacy_message"]
    elif language == "es":
        privacy_message = strings_es["privacy_message"]
    elif language == "jap":
        privacy_message = strings_jap["privacy_message"]
    elif language == "ko":
        privacy_message = strings_ko["privacy_message"]
    elif language == "zh_hans":
        privacy_message = strings_zh_hans["privacy_message"]
    elif language == "zh_hant":
        privacy_message = strings_zh_hant["privacy_message"]

    await bot.send_message(
        chat_id=message.chat.id,
        text=privacy_message.format(bot_username=bot_username),
        parse_mode="HTML",
        protect_content=True
    )