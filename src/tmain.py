import telebot

from config import settings

token = settings.TOKEN
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, 'Hi 👾')
    bot.send_message(message.chat.id, 'ヾ(•ω•`)o')


bot.infinity_polling()
