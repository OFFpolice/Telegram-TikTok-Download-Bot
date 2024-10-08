from aiogram import types
from aiogram.dispatcher import FSMContext
from dispatcher import dp, admin_id
from class_distribution import DistributionState
from database import get_user_language
from load_language import load_language_files


@dp.message_handler(content_types=["document", "video", "audio", "voice", "animation", "photo", "text"], state=DistributionState.WaitForMedia, user_id=admin_id)
async def handle_media(message: types.Message, state: FSMContext):
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

    async with state.proxy() as data:
        data["media"] = message
        keyboard = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("✅", callback_data="confirm_media"),
            types.InlineKeyboardButton("❌", callback_data="cancel_media"))
        await DistributionState.ConfirmMedia.set()
        user_id = message.from_user.id
        language = await get_user_language(user_id)
        messages = {
            "ru": strings_ru["check_broadcast"],
            "en": strings_en["check_broadcast"],
            "uk": strings_uk["check_broadcast"],
            "de": strings_de["check_broadcast"],
            "fr": strings_fr["check_broadcast"],
            "es": strings_es["check_broadcast"],
            "jap": strings_jap["check_broadcast"],
            "ko": strings_ko["check_broadcast"],
            "zh_hans": strings_zh_hans["check_broadcast"],
            "zh_hant": strings_zh_hant["check_broadcast"],
        }
        check_template = messages.get(language, "")
        await message.reply(check_template, parse_mode="HTML", protect_content=True, reply_markup=keyboard)
