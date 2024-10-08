from aiogram import types

# Создание клавиатуры для выбора языка
keyboard_language = types.InlineKeyboardMarkup(row_width=2)
# Первая строка языков
keyboard_language.add(
    types.InlineKeyboardButton(text="🇺🇦 Українська", callback_data="set_language_uk"),
    types.InlineKeyboardButton(text="🇬🇧 English", callback_data="set_language_en")
)
# Вторая строка языков
keyboard_language.add(
    types.InlineKeyboardButton(text="🇷🇺 Русский", callback_data="set_language_ru"),
    types.InlineKeyboardButton(text="🇩🇪 Deutsch", callback_data="set_language_de")
)
# Третья строка языков
keyboard_language.add(
    types.InlineKeyboardButton(text="🇫🇷 Français", callback_data="set_language_fr"),
    types.InlineKeyboardButton(text="🇪🇸 Español", callback_data="set_language_es")
)
# Четвертая строка языков
keyboard_language.add(
    types.InlineKeyboardButton(text="🇯🇵 日本語", callback_data="set_language_jap"),
    types.InlineKeyboardButton(text="🇰🇷 한국인", callback_data="set_language_ko")
)
# Пятая строка языков
keyboard_language.add(
    types.InlineKeyboardButton(text="🇨🇳 中国人", callback_data="set_language_zh_hans"),
    types.InlineKeyboardButton(text="🇨🇳 中國人", callback_data="set_language_zh_hant")
)

# Создание клавиатуры для TikTok Web
tiktok_web = types.InlineKeyboardMarkup(row_width=1)
tiktok_web.add(
    types.InlineKeyboardButton(text="Open App", web_app=types.WebAppInfo(url="https://www.tiktok.com/en"))
)

# Создание клавиатуры для Shazam Bot
url_button = types.InlineKeyboardMarkup()
url_button.add(
    types.InlineKeyboardButton(text="🌀 Shazam Bot", url="https://telegram.me/OFFpoliceShazamBot?start=tiktokbot")
)

# Асинхронная функция для создания status_button на основе языка
async def create_status_button(strings, channel_link):
    status_button = types.InlineKeyboardMarkup()
    status_button.add(types.InlineKeyboardButton(text=strings["button_url"], url=channel_link))
    status_button.row(types.InlineKeyboardButton(text=strings["button_check"], callback_data="check_subscription"))
    return status_button
