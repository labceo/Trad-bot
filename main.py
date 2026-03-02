import os
import telebot
import time

# Получаем токен из переменных окружения
TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN is None:
    print("❌ Ошибка: Токен не найден!")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Дарова! Я Традиционный Бот. Работаю 24/7 на Render!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Спроси меня про: скинхедов, карланов, Thor Steinar, Lonsdale, Stone Island")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if 'скинхед' in text:
        bot.reply_to(message, "🇬🇧 Субкультура зародилась в 1960х в Британии. Сначала были традиционные скинхеды против буржуазии. В 80х появились бонхеды из-за кризиса и мигрантов.")
    elif 'карлан' in text:
        bot.reply_to(message, "Дарова! Карланы — позеры, носят паленку, не знают историю брендов и не могут пояснить за шмот.")
    elif 'тор штайнер' in text or 'thor steinar' in text:
        bot.reply_to(message, "Thor Steinar — отсылка к скандинавской мифологии (Тор). Популярен среди правых, но бренд заявляет об аполитичности.")
    elif 'лонсдейл' in text or 'lonsdale' in text:
        bot.reply_to(message, "Lonsdale — британский боксёрский бренд с 1960. Буквы NSL дали повод для шуток, но бренд аполитичен.")
    elif 'стоун айленд' in text or 'stone island' in text:
        bot.reply_to(message, "Stone Island — итальянский бренд с 1982. Компас символизирует исследования. Технологичный, модный, аполитичный.")
    elif 'аполитичн' in text:
        bot.reply_to(message, "Аполитичные: Stone Island, Lonsdale, Fred Perry, Alpha Industries. Неаполитичный: Thor Steinar (из-за символики).")
    else:
        bot.reply_to(message, "Напиши: скинхеды, карланы, thor steinar, lonsdale, stone island")

print("✅ Бот запущен на Render! Жду сообщения...")

# Запускаем бота
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Ошибка: {e}")import os
import telebot
import time

# Получаем токен из переменных окружения
TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN is None:
    print("❌ Ошибка: Токен не найден!")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Дарова! Я Традиционный Бот. Работаю 24/7 на Render!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Спроси меня про: скинхедов, карланов, Thor Steinar, Lonsdale, Stone Island")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if 'скинхед' in text:
        bot.reply_to(message, "🇬🇧 Субкультура зародилась в 1960х в Британии. Сначала были традиционные скинхеды против буржуазии. В 80х появились бонхеды из-за кризиса и мигрантов.")
    elif 'карлан' in text:
        bot.reply_to(message, "Дарова! Карланы — позеры, носят паленку, не знают историю брендов и не могут пояснить за шмот.")
    elif 'тор штайнер' in text or 'thor steinar' in text:
        bot.reply_to(message, "Thor Steinar — отсылка к скандинавской мифологии (Тор). Популярен среди правых, но бренд заявляет об аполитичности.")
    elif 'лонсдейл' in text or 'lonsdale' in text:
        bot.reply_to(message, "Lonsdale — британский боксёрский бренд с 1960. Буквы NSL дали повод для шуток, но бренд аполитичен.")
    elif 'стоун айленд' in text or 'stone island' in text:
        bot.reply_to(message, "Stone Island — итальянский бренд с 1982. Компас символизирует исследования. Технологичный, модный, аполитичный.")
    elif 'аполитичн' in text:
        bot.reply_to(message, "Аполитичные: Stone Island, Lonsdale, Fred Perry, Alpha Industries. Неаполитичный: Thor Steinar (из-за символики).")
    else:
        bot.reply_to(message, "Напиши: скинхеды, карланы, thor steinar, lonsdale, stone island")

print("✅ Бот запущен на Render! Жду сообщения...")

# Запускаем бота
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
