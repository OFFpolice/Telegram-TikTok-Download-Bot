from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot, admin_id
from class_distribution import DistributionState
from database import get_user_language
from load_language import load_language_files


@dp.callback_query_handler(Text(equals="cancel_media"), state=DistributionState.ConfirmMedia, user_id=admin_id)
async def cancel_media(callback_query: types.CallbackQuery, state: FSMContext):
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
    language = await get_user_language(user_id)
    await state.finish()
    await callback_query.message.edit_reply_markup()
    if language == "ru":
        await bot.answer_callback_query(callback_query.id, strings_ru["off_broadcast"], show_alert=True)
    elif language == "en":
        await bot.answer_callback_query(callback_query.id, strings_en["off_broadcast"], show_alert=True)
    elif language == "uk":
        await bot.answer_callback_query(callback_query.id, strings_uk["off_broadcast"], show_alert=True)
    elif language == "de":
        await bot.answer_callback_query(callback_query.id, strings_de["off_broadcast"], show_alert=True)
    elif language == "fr":
        await bot.answer_callback_query(callback_query.id, strings_fr["off_broadcast"], show_alert=True)
    elif language == "es":
        await bot.answer_callback_query(callback_query.id, strings_es["off_broadcast"], show_alert=True)
    elif language == "jap":
        await bot.answer_callback_query(callback_query.id, strings_jap["off_broadcast"], show_alert=True)
    elif language == "ko":
        await bot.answer_callback_query(callback_query.id, strings_ko["off_broadcast"], show_alert=True)
    elif language == "zh_hans":
        await bot.answer_callback_query(callback_query.id, strings_zh_hans["off_broadcast"], show_alert=True)
    elif language == "zh_hant":
        await bot.answer_callback_query(callback_query.id, strings_zh_hant["off_broadcast"], show_alert=True)
