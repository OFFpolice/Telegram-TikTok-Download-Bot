import os
import random
import logging

from aiogram import types
from dispatcher import dp, bot, photo_url, channel_link, channel_id
from database import get_user_language, add_new_download, get_saved_video, add_new_download_count
from download import download_video
from random_id import sticker_id
from load_language import load_language_files
from keyboards import url_button, create_status_button


@dp.message_handler(regexp=r"https://[a-zA-Z]+.tiktok.com/")
async def tiktok_download(message: types.Message):
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

    channel_member = await bot.get_chat_member(channel_id, message.chat.id)
    if channel_member.status == "left":
        if language == "ru":
            strings = strings_ru
        elif language == "en":
            strings = strings_en
        elif language == "uk":
            strings = strings_uk
        elif language == "de":
            strings = strings_de
        elif language == "fr":
            strings = strings_fr
        elif language == "es":
            strings = strings_es
        elif language == "jap":
            strings = strings_jap
        elif language == "ko":
            strings = strings_ko
        elif language == "zh_hans":
            strings = strings_zh_hans
        elif language == "zh_hant":
            strings = strings_zh_hant

        status_button = await create_status_button(strings, channel_link)
        caption_check = strings["text_check"]

        await bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=caption_check, reply_markup=status_button, parse_mode="HTML", protect_content=True)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    saved_video = await get_saved_video(message.text)
    if saved_video:
        await bot.send_video(chat_id=message.chat.id, video=saved_video["file_id"], caption=saved_video["caption"], parse_mode="HTML", reply_markup=url_button)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    try:
        if language == "ru":
            processing = strings_ru["processing"]
        elif language == "en":
            processing = strings_en["processing"]
        elif language == "uk":
            processing = strings_uk["processing"]
        elif language == "de":
            processing = strings_de["processing"]
        elif language == "fr":
            processing = strings_fr["processing"]
        elif language == "es":
            processing = strings_es["processing"]
        elif language == "jap":
            processing = strings_jap["processing"]
        elif language == "ko":
            processing = strings_ko["processing"]
        elif language == "zh_hans":
            processing = strings_zh_hans["processing"]
        elif language == "zh_hant":
            processing = strings_zh_hant["processing"]

        random_sticker = random.choice(sticker_id)
        sticker_message = await bot.send_sticker(chat_id=message.chat.id, sticker=random_sticker, protect_content=True)
        processing_message = await bot.send_message(chat_id=message.chat.id, text=processing, parse_mode="HTML", protect_content=True)

        video_path, description, channel_url, channel_name, post_link = await download_video(message.text)

        await bot.send_chat_action(message.chat.id, "upload_video")

        if language == "ru":
            video_caption = strings_ru["video_caption"]
        elif language == "en":
            video_caption = strings_en["video_caption"]
        elif language == "uk":
            video_caption = strings_uk["video_caption"]
        elif language == "de":
            video_caption = strings_de["video_caption"]
        elif language == "fr":
            video_caption = strings_fr["video_caption"]
        elif language == "es":
            video_caption = strings_es["video_caption"]
        elif language == "jap":
            video_caption = strings_jap["video_caption"]
        elif language == "ko":
            video_caption = strings_ko["video_caption"]
        elif language == "zh_hans":
            video_caption = strings_zh_hans["video_caption"]
        elif language == "zh_hant":
            video_caption = strings_zh_hant["video_caption"]

        video_caption = video_caption.format(description=description, channel_url=channel_url, channel_name=channel_name, post_link=post_link, bot_username=bot_username)

        video_file = types.InputFile(video_path)
        sent_message = await bot.send_video(chat_id=message.chat.id, video=video_file, caption=video_caption, parse_mode="HTML", reply_markup=url_button)
        file_id = sent_message.video.file_id

        await add_new_download(message.text, file_id, video_caption)
        await add_new_download_count()

        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=sticker_message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
        os.remove(video_path)

    except Exception as e:
        logging.error(e)
        print(e)
        if language == "ru":
            error_message = strings_ru["error_message"]
        elif language == "en":
            error_message = strings_en["error_message"]
        elif language == "uk":
            error_message = strings_uk["error_message"]
        elif language == "de":
            error_message = strings_de["error_message"]
        elif language == "fr":
            error_message = strings_fr["error_message"]
        elif language == "es":
            error_message = strings_es["error_message"]
        elif language == "jap":
            error_message = strings_jap["error_message"]
        elif language == "ko":
            error_message = strings_ko["error_message"]
        elif language == "zh_hans":
            error_message = strings_zh_hans["error_message"]
        elif language == "zh_hant":
            error_message = strings_zh_hant["error_message"]
        await bot.send_message(chat_id=message.chat.id, text=error_message, parse_mode="HTML", protect_content=True)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=sticker_message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
        os.remove(video_path)
