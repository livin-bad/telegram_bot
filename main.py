import os
import telebot

bot = telebot.TeleBot('2122699164:AAE8CSXemfVfZ0tJMEGYvEyDKWVDec_BpNY')


@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, 'hey! this is test msg')


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.reply_to(message, 'Hello!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    if message.text == 'Hi':
        # bot.send_message(message.chat.id, 'hi there')
        bot.reply_to(message, 'Hi')
    elif message.text == "Are you a boy?":
        bot.reply_to(message, 'Yes')
    # else:
    #     bot.reply_to(message, '404')


bot.polling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
