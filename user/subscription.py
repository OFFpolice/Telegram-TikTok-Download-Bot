import logging

from aiogram import types
from dispatcher import dp, bot, channel_id
from database import get_user_language
from load_language import load_language_files


@dp.callback_query_handler(lambda query: query.data == "check_subscription")
async def check_subscription(callback_query: types.CallbackQuery):
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

    user_id = callback_query.from_user.id
    try:
        channel_member = await bot.get_chat_member(channel_id, user_id)
        language = await get_user_language(user_id)
        if language == "ru":
            success_message = strings_ru["success_message"]
            failure_message = strings_ru["failure_message"]
        elif language == "en":
            success_message = strings_en["success_message"]
            failure_message = strings_en["failure_message"]
        elif language == "uk":
            success_message = strings_uk["success_message"]
            failure_message = strings_uk["failure_message"]
        elif language == "de":
            success_message = strings_de["success_message"]
            failure_message = strings_de["failure_message"]
        elif language == "fr":
            success_message = strings_fr["success_message"]
            failure_message = strings_fr["failure_message"]
        elif language == "es":
            success_message = strings_es["success_message"]
            failure_message = strings_es["failure_message"]
        elif language == "jap":
            success_message = strings_jap["success_message"]
            failure_message = strings_jap["failure_message"]
        elif language == "ko":
            success_message = strings_ko["success_message"]
            failure_message = strings_ko["failure_message"]
        elif language == "zh_hans":
            success_message = strings_zh_hans["success_message"]
            failure_message = strings_zh_hans["failure_message"]
        elif language == "zh_hant":
            success_message = strings_zh_hant["success_message"]
            failure_message = strings_zh_hant["failure_message"]
        if channel_member.status == "member":
            await bot.answer_callback_query(callback_query.id, text=success_message, show_alert=True)
            await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
        else:
            await bot.answer_callback_query(callback_query.id, text=failure_message, show_alert=True)
    except Exception as e:
        logging.error(e)
        print(e)
