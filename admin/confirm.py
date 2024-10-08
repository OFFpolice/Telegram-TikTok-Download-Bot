import re
import time
import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot, admin_id
from class_distribution import DistributionState
from database import get_user_language, get_users
from load_language import load_language_files


@dp.callback_query_handler(Text(equals="confirm_media"), state=DistributionState.ConfirmMedia, user_id=admin_id)
async def confirm_media(callback_query: types.CallbackQuery, state: FSMContext):
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
        user_id = data["user_id"]
        media = data["media"]
        text_message = data.get("text_message")
        async def throttle_send(delay):
            nonlocal last_sent_time
            current_time = time.time()
            time_since_last_sent = current_time - last_sent_time
            if time_since_last_sent < delay:
                await asyncio.sleep(delay - time_since_last_sent)
            last_sent_time = time.time()
        user_id = data["user_id"]
        language = await get_user_language(user_id)
        messages = {
            "ru": {"start_broadcast": strings_ru["start_broadcast"], "media_too_large": strings_ru["media_too_large"], "broadcast_completed": strings_ru["broadcast_completed"]},
            "en": {"start_broadcast": strings_en["start_broadcast"], "media_too_large": strings_en["media_too_large"], "broadcast_completed": strings_en["broadcast_completed"]},
            "uk": {"start_broadcast": strings_uk["start_broadcast"], "media_too_large": strings_uk["media_too_large"], "broadcast_completed": strings_uk["broadcast_completed"]},
            "de": {"start_broadcast": strings_de["start_broadcast"], "media_too_large": strings_de["media_too_large"], "broadcast_completed": strings_de["broadcast_completed"]},
            "fr": {"start_broadcast": strings_fr["start_broadcast"], "media_too_large": strings_fr["media_too_large"], "broadcast_completed": strings_fr["broadcast_completed"]},
            "es": {"start_broadcast": strings_es["start_broadcast"], "media_too_large": strings_es["media_too_large"], "broadcast_completed": strings_es["broadcast_completed"]},
            "jap": {"start_broadcast": strings_jap["start_broadcast"], "media_too_large": strings_jap["media_too_large"], "broadcast_completed": strings_jap["broadcast_completed"]},
            "ko": {"start_broadcast": strings_ko["start_broadcast"], "media_too_large": strings_ko["media_too_large"], "broadcast_completed": strings_ko["broadcast_completed"]},
            "zh_hans": {"start_broadcast": strings_zh_hans["start_broadcast"], "media_too_large": strings_zh_hans["media_too_large"], "broadcast_completed": strings_zh_hans["broadcast_completed"]},
            "zh_hant": {"start_broadcast": strings_zh_hant["start_broadcast"], "media_too_large": strings_zh_hant["media_too_large"], "broadcast_completed": strings_zh_hant["broadcast_completed"]}
        }
        language_messages = messages.get(language, "")
        await callback_query.message.edit_reply_markup()
        await bot.send_message(user_id, language_messages["start_broadcast"], parse_mode="HTML", protect_content=True)
        users_list = await get_users()
        media_id = None
        media_type = None
        media_size = 0
        if media.document:
            media_id = media.document.file_id
            media_type = "document"
            media_size = media.document.file_size
        elif media.video:
            media_id = media.video.file_id
            media_type = "video"
            media_size = media.video.file_size
        elif media.audio:
            media_id = media.audio.file_id
            media_type = "audio"
            media_size = media.audio.file_size
        elif media.voice:
            media_id = media.voice.file_id
            media_type = "voice"
            media_size = media.voice.file_size
        elif media.animation:
            media_id = media.animation.file_id
            media_type = "animation"
            media_size = media.animation.file_size
        elif media.photo:
            media_id = media.photo[-1].file_id
            media_type = "photo"
            media_size = 0
        elif media.text:
            media_type = "text"
            text_message = media.text
        if media_size <= 10 * 1024 * 1024:
            last_sent_time = 0
            media_sent = 0
            block_users = 0
            for user in users_list:
                await throttle_send(1)
                caption = media.caption
                if caption:
                    caption = re.sub(r"([\\_~`>#+\-|=|{}()\[\].!])", r"\\\1", caption)
                try:
                    if media_type == "text":
                        await bot.send_message(user, text_message, parse_mode=types.ParseMode.MARKDOWN, protect_content=True)
                    elif media_type == "photo":
                        await bot.send_photo(user, photo=media_id, caption=caption, parse_mode=types.ParseMode.MARKDOWN_V2, protect_content=True)
                    else:
                        await bot.send_document(user, document=media_id, caption=caption, parse_mode=types.ParseMode.MARKDOWN_V2, protect_content=True)
                    media_sent += 1
                    last_sent_time = time.time()
                except:
                    block_users += 1
            completed_message = language_messages["broadcast_completed"].format(media_sent=media_sent, block_users=block_users)
            await bot.send_message(user_id, completed_message, parse_mode="HTML",protect_content=True)
        else:
            await bot.send_message(user_id, language_messages["media_too_large"], parse_mode="HTML", protect_content=True)
        await state.finish()
