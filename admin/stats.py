from aiogram import types
from dispatcher import dp, admin_id
from database import get_user_language, get_users_count, get_downloads
from load_language import load_language_files


@dp.message_handler(commands=["stats"], user_id=admin_id)
async def stats_command(message: types.Message):
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
    downloads_count = await get_downloads()
    users_count = int(await get_users_count())
    strings = {
        "ru": strings_ru["stats_admin"],
        "uk": strings_uk["stats_admin"],
        "en": strings_en["stats_admin"],
        "de": strings_de["stats_admin"],
        "fr": strings_fr["stats_admin"],
        "es": strings_es["stats_admin"],
        "jap": strings_jap["stats_admin"],
        "ko": strings_ko["stats_admin"],
        "zh_hans": strings_zh_hans["stats_admin"],
        "zh_hant": strings_zh_hant["stats_admin"],
    }
    stats_template = strings.get(language, "")
    await message.answer(stats_template.format(users_count=users_count, downloads_count=downloads_count), parse_mode="HTML", protect_content=True)
