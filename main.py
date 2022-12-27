from pprint import pprint

import telebot
import random

from addon import stab
from config import const
from config import env

bot = telebot.TeleBot(env.TELEGRAMBOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['pick'])
def select_bot(message):
    for seperator in const.PICK_SEPERATOR:
        if seperator in message.text:
            msg = message.text.split(seperator)
            bot.reply_to(message, random.choice(msg))


@bot.message_handler(commands=['stab'])
def stabbing(message):
    bot.reply_to(message, stab.stab(str(message.from_user.id), str(message.chat.id), message.text.split()[1]))


@bot.message_handler(commands=['register_stab'])
def register_stab(message):
    register_message = stab.register_stab(str(message.from_user.id), str(message.chat.id))
    bot.reply_to(message, register_message)


@bot.message_handler(commands=['stab_keyword'])
def post_stab_keyword(message):
    print(message.text)
    if stab.check_stab_list(str(message.from_user.id), str(message.chat.id)):
        if len(message.text.split()) == 1:
            bot.reply_to(message, "키워드를 등록해주세요")
            return
        bot.reply_to(message,
                     stab.fetch_keyword(str(message.chat.id), str(message.from_user.id), message.text.split()[1]))
    else:
        bot.reply_to(message, "등록되지 않은 유저입니다.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    pprint(str(message))

    if const.CONCH_MEAT in message.text:
        bot.reply_to(message, random.choice([const.POSITIVE_ANSWER, const.NEGATIVE_ANSWER]))

    if const.PERCENTAGE in message.text:
        bot.reply_to(message, str(random.randint(0, 100)) + const.PERCENTAGE_STR)


bot.infinity_polling()
