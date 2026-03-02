import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN is None:
    print("Ошибка: токен не найден")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Дарова! Я Традиционный Бот")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if 'скинхед' in text:
        bot.reply_to(message, "🇬🇧 Субкультура зародилась в 1960х в Британии. Сначала были традиционные скинхеды против буржуазии. В 80х появились бонхеды из-за кризиса и мигрантов.")
    
    elif 'карлан' in text:
        bot.reply_to(message, "Дарова! Карланы — позеры, носят паленку, не знают историю брендов и не могут пояснить за шмот.")
    
    elif 'тор штайнер' in text or 'thor steinar' in text:
        bot.reply_to(message, "Thor Steinar — немецкий бренд с 1999. Отсылка к скандинавской мифологии (Тор). Из-за символики ассоциировался с правыми, но бренд заявляет об аполитичности.")
    
    elif 'лонсдейл' in text or 'lonsdale' in text:
        bot.reply_to(message, "Lonsdale — британский боксёрский бренд с 1960. Назван в честь графа Лонсдейла. Аполитичный, но из-за букв NSL был популярен среди скинхедов.")
    
    elif 'стоун айленд' in text or 'stone island' in text:
        bot.reply_to(message, "Stone Island — итальянский бренд с 1982. Компас символизирует исследования. Знаменит технологичными тканями. Аполитичный.")
    
    else:
        bot.reply_to(message, "Напиши: скинхеды, карланы, thor steinar, lonsdale, stone island")

print("Бот запущен!")
bot.polling(none_stop=True)
