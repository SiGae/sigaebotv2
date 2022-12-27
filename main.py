from pprint import pprint

import telebot
import random

from config import const
from config import env

bot = telebot.TeleBot(env.TELEGRAMBOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['pick'])
def select_bot(message):
    for seperator in const.PICK_SEPERATOR:
        if seperator in message.text:
            msg = message.text.split(seperator)
            bot.reply_to(message, random.choice(msg))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    pprint(str(message))

    if const.CONCH_MEAT in message.text:
        bot.reply_to(message, random.choice([const.POSITIVE_ANSWER, const.NEGATIVE_ANSWER]))

bot.infinity_polling()
