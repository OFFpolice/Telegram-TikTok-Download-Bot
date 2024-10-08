import asyncio

from aiogram import executor, types
from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot, admin_id
from database import database_initialization
from class_distribution import DistributionState

from admin.admin import admin_command
from admin.stats import stats_command
from admin.send import send_command
from admin.handle import handle_media
from admin.confirm import confirm_media
from admin.cancel import cancel_media

from user.start import start_command
from user.lang import lang_command
from user.privacy import privacy_command
from user.tiktok import tiktok_download
from user.subscription import check_subscription
from user.set_lang import set_language


async def register_admin_handlers():
    dp.register_message_handler(
        admin_command,
        commands=["admin"],
        user_id=admin_id
    )
    dp.register_message_handler(
        stats_command,
        commands=["stats"],
        user_id=admin_id
    )
    dp.register_message_handler(
        send_command,
        commands=["send"],
        user_id=admin_id
    )
    dp.register_message_handler(
        handle_media,
        content_types=[
            "document",
            "video",
            "audio",
            "voice",
            "animation",
            "photo",
            "text"
        ],
        state=DistributionState.WaitForMedia,
        user_id=admin_id
    )
    dp.register_message_handler(
        confirm_media,
        Text(equals="confirm_media"),
        state=DistributionState.ConfirmMedia,
        user_id=admin_id
    )
    dp.register_message_handler(
        cancel_media,
        Text(equals="cancel_media"),
        state=DistributionState.ConfirmMedia,
        user_id=admin_id
    )


async def register_user_handlers():
    dp.register_message_handler(
        start_command,
        commands=["start"]
    )
    dp.register_message_handler(
        lang_command,
        commands=["lang"]
    )
    dp.register_message_handler(
        privacy_command,
        commands=["privacy"]
    )
    dp.register_message_handler(
        tiktok_download,
        regexp=r"https://[a-zA-Z]+.tiktok.com/"
    )
    dp.register_message_handler(
        check_subscription,
        lambda query: query.data == "check_subscription"
    )
    dp.register_message_handler(
        set_language,
        lambda query: query.data in [
            "set_language_ru",
            "set_language_en",
            "set_language_uk",
            "set_language_de",
            "set_language_fr",
            "set_language_es",
            "set_language_jap",
            "set_language_ko",
            "set_language_zh_hans",
            "set_language_zh_hant"
        ]
    )


async def set_commands():
    user_commands = [
        types.BotCommand(
            command="/start",
            description="🤖 Start"
        ),
        types.BotCommand(
            command="/lang",
            description="🌏 Lang"
        ),
        types.BotCommand(
            command="/privacy",
            description="👤 Privacy Policy"
        )
    ]
    admin_commands = [
        types.BotCommand(
            command="/start",
            description="🤖 Start"
        ),
        types.BotCommand(
            command="/lang",
            description="🌏 Lang"
        ),
        types.BotCommand(
            command="/privacy",
            description="👤 Privacy Policy"
        ),
        types.BotCommand(
            command="/admin",
            description="🎛 Admin menu"
        )
    ]
    await bot.set_my_commands(
        user_commands,
        scope=types.BotCommandScopeDefault(
        )
    )
    await bot.set_my_commands(
        admin_commands,
        scope=types.BotCommandScopeChat(
        chat_id=admin_id
        )
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(database_initialization())
    loop.run_until_complete(register_admin_handlers())
    loop.run_until_complete(register_user_handlers())
    loop.run_until_complete(set_commands())
    executor.start_polling(dp, skip_updates=True)
