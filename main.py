import telebot

bot = telebot.TeleBot('6758333739:AAGC4Tut-Wr3DnivKqMtgC3hYAED7ujlM_8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'миу')


@bot.message_handler(commands=['drop'])
def main(message):
    bot.send_message(message.chat.id, 'девочка Уенздей')


@bot.message_handler(commands=['push'])
def main(message):
    bot.send_message(message.chat.id, 'завтра в школу')


@bot.message_handler(commands=['top'])
def main(message):
    bot.send_message(message.chat.id, 'Умскул лучшие!!!')


@bot.message_handler(commands=['good'])
def main(message):
    bot.send_message(message.chat.id, 'хорошего дня')


bot.infinity_polling()
