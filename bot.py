import os
import logging
from urllib.parse import urlparse, urlunparse

import telebot
from telebot import apihelper
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан. Укажите его в файле .env")

PROXY_URL = os.getenv("PROXY_URL", "").strip()
if PROXY_URL:
    apihelper.proxy = {"http": PROXY_URL, "https": PROXY_URL}
    parsed = urlparse(PROXY_URL)
    safe_proxy = urlunparse(parsed._replace(netloc=parsed.hostname if not parsed.port else f"{parsed.hostname}:{parsed.port}"))
    logger.info("Прокси настроен: %s", safe_proxy)
else:
    logger.info("Прокси не используется")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message: telebot.types.Message) -> None:
    bot.reply_to(message, "Привет! Я работаю.")


@bot.message_handler(func=lambda m: True)
def handle_message(message: telebot.types.Message) -> None:
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    logger.info("Бот запущен. Нажмите Ctrl+C для остановки.")
    bot.infinity_polling(timeout=30, long_polling_timeout=20)
