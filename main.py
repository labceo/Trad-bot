import os
import telebot
import time

TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN is None:
    print("Ошибка: токен не найден")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Дарова! Я Традиционный Бот. Работаю 24/7!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Спроси про: скинхедов, карланов, бренды")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if 'скинхед' in text:
        bot.reply_to(message, "Субкультура зародилась в 1960х в Британии. Сначала традиционные скинхеды против буржуазии. В 80х появились бонхеды из-за кризиса и мигрантов.")
    elif 'карлан' in text:
        bot.reply_to(message, "Дарова! Карланы — позеры, носят паленку, не знают историю брендов.")
    elif 'тор штайнер' in text or 'thor steinar' in text:
        bot.reply_to(message, "Thor Steinar — отсылка к скандинавской мифологии (Тор). Бренд заявляет об аполитичности.")
    elif 'лонсдейл' in text or 'lonsdale' in text:
        bot.reply_to(message, "Lonsdale — британский боксёрский бренд с 1960. Аполитичный.")
    elif 'стоун айленд' in text or 'stone island' in text:
        bot.reply_to(message, "Stone Island — итальянский бренд с 1982. Компас символизирует исследования. Аполитичный.")
    else:
        bot.reply_to(message, "Напиши: скинхеды, карланы, thor steinar, lonsdale, stone island")

print("Бот запущен!")
bot.polling(none_stop=True)
