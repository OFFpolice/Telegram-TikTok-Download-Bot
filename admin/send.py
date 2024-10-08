from aiogram import types
from aiogram.dispatcher import FSMContext
from dispatcher import dp, admin_id
from class_distribution import DistributionState
from database import get_user_language
from load_language import load_language_files


@dp.message_handler(commands=["send"], user_id=admin_id)
async def send_command(message: types.Message, state: FSMContext):
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
        data["user_id"] = message.chat.id
    await DistributionState.WaitForMedia.set()
    user_id = message.from_user.id
    language = await get_user_language(user_id)
    strings = {
        "ru": strings_ru["send_admin"],
        "en": strings_en["send_admin"],
        "uk": strings_uk["send_admin"],
        "de": strings_de["send_admin"],
        "fr": strings_fr["send_admin"],
        "es": strings_es["send_admin"],
        "jap": strings_jap["send_admin"],
        "ko": strings_ko["send_admin"],
        "zh_hans": strings_zh_hans["send_admin"],
        "zh_hant": strings_zh_hant["send_admin"]
    }
    send_template = strings.get(language, "")
    await message.answer(send_template, parse_mode="HTML", protect_content=True)
