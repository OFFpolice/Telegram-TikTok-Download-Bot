import os
import logging

from dotenv import load_dotenv
from os.path import join, dirname

from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


channel_link = os.environ.get("channel_link")
channel_id = os.environ.get("channel_id")
bot_token = os.environ.get("bot_token")
admin_id = os.environ.get("admin_id")
photo_url = os.environ.get("photo_url")
animation_url = os.environ.get("animation_url")


bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
    filename="run.log"
)
