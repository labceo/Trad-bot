import os
import telebot
import time

TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN is None:
    print("❌ Ошибка: Токен не найден!")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Дарова! Я Традиционный Бот. Работаю 24/7 на Render!")

# ... остальной код (я сократил для примера)
