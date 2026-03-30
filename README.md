# glinux_peresdacha

Учебный проект по курсу **Linux & DevOps**. Демонстрирует CI/CD с помощью GitHub Actions, а также содержит основы работы с Telegram-ботом.

---

## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Запуск консольного приложения](#запуск-консольного-приложения)
- [Запуск тестов](#запуск-тестов)
- [Telegram-бот](#telegram-бот)
  - [Как получить токен](#как-получить-токен)
  - [Настройка токена](#настройка-токена)
  - [Запуск бота](#запуск-бота)
- [CI/CD](#cicd)

---

## Требования

- Python 3.8+
- pip

---

## Установка

```bash
git clone https://github.com/Mag1cMouse/glinux_peresdacha.git
cd glinux_peresdacha
pip install -r requirements.txt
```

---

## Запуск консольного приложения

```bash
python main.py
```

Пример вывода:

```
=== Консольное приложение ===
Привет, Мир!
2 + 3 = 5
4 * 5 = 20

Информация о проекте:
  author: Student
  subject: Linux & DevOps
  topic: CI/CD with GitHub Actions
```

---

## Запуск тестов

```bash
pip install pytest
pytest test_main.py -v
```

---

## Telegram-бот

### Как получить токен

1. Откройте Telegram и найдите [@BotFather](https://t.me/BotFather).
2. Отправьте команду `/newbot` и следуйте инструкциям.
3. После создания бота BotFather пришлёт **API-токен** (строка вида `1234567890:AAXXXXXXXX...`).

> ⚠️ **Никогда не публикуйте токен в коде или в публичных репозиториях.** Любой, кто получит токен, сможет управлять вашим ботом.

### Настройка токена

Токен передаётся через переменную окружения `TELEGRAM_BOT_TOKEN`. Это безопасный способ — токен не попадает в исходный код.

**Linux / macOS (терминал):**

```bash
export TELEGRAM_BOT_TOKEN="ваш_токен_здесь"
```

**Windows (PowerShell):**

```powershell
$env:TELEGRAM_BOT_TOKEN = "ваш_токен_здесь"
```

**Файл `.env` (для локальной разработки):**

Создайте файл `.env` в корне проекта (он уже добавлен в `.gitignore`):

```
TELEGRAM_BOT_TOKEN=ваш_токен_здесь
```

Затем загрузите его перед запуском:

```bash
pip install python-dotenv
```

И в коде бота:

```python
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
```

**GitHub Actions (для CI/CD):**

1. Перейдите в `Settings → Secrets and variables → Actions` вашего репозитория.
2. Нажмите **New repository secret**.
3. Имя: `TELEGRAM_BOT_TOKEN`, значение: ваш токен.
4. В файле воркфлоу используйте: `${{ secrets.TELEGRAM_BOT_TOKEN }}`.

### Запуск бота

После настройки переменной окружения:

```bash
python bot.py
```

Файл `bot.py` в корне репозитория читает токен из переменной окружения и запускает бота со следующими командами:

| Команда  | Описание                        |
|----------|---------------------------------|
| `/start` | Приветствие и список команд     |
| `/help`  | Список доступных команд         |
| `/info`  | Информация о проекте            |

Любое текстовое сообщение бот повторяет обратно.

Код `bot.py`:

```python
from dotenv import load_dotenv
import os
import telebot

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(message, "Привет! 👋")

bot.infinity_polling()
```

---

## CI/CD

Проект использует **GitHub Actions** для автоматического запуска тестов при каждом push и pull request. Конфигурация находится в `.github/workflows/`.
