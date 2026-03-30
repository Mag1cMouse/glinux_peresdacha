import os
import sys

from dotenv import load_dotenv
import telebot

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")

if not token:
    print(
        "Ошибка: переменная окружения TELEGRAM_BOT_TOKEN не задана.\n"
        "Создайте файл .env в корне проекта и добавьте в него:\n"
        "  TELEGRAM_BOT_TOKEN=ваш_токен_здесь\n"
        "Или экспортируйте переменную вручную:\n"
        "  export TELEGRAM_BOT_TOKEN=ваш_токен_здесь"
    )
    sys.exit(1)

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(
        message,
        "Привет! 👋 Я учебный Telegram-бот проекта glinux_peresdacha.\n\n"
        "Доступные команды:\n"
        "  /start — приветствие\n"
        "  /help  — список команд\n"
        "  /info  — информация о проекте",
    )


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.reply_to(
        message,
        "Список доступных команд:\n"
        "  /start — приветствие\n"
        "  /help  — список команд\n"
        "  /info  — информация о проекте",
    )


@bot.message_handler(commands=["info"])
def handle_info(message):
    bot.reply_to(
        message,
        "📋 Информация о проекте:\n"
        "  Автор:   Student\n"
        "  Курс:    Linux & DevOps\n"
        "  Тема:    CI/CD with GitHub Actions",
    )


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, f"Вы написали: {message.text}\nОтправьте /help чтобы увидеть список команд.")


if __name__ == "__main__":
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    bot.infinity_polling()
