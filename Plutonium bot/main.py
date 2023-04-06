import telebot
from bot_key import key
from callback_operation import callback_op
from users_sort import users_sort

bot = telebot.TeleBot(key)


@bot.message_handler(content_types=['text'])
def sorting_users(msg):
    users_sort(bot, msg)


@bot.message_handler(content_types=['sticker'])
def anti_sticker(msg):
    bot.send_message(msg.chat.id, "Каждый раз, когда вы отправляете мне стикер, в мире погибает 1 котенок(😿")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    callback_op(bot, call)


bot.polling(none_stop=True, interval=1)
