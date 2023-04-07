import telebot
from bot_key import key
from callback_operation import callback_op
from users_sort import users_sorting
import sqlite3
from registration import register
from callback_operation import pic_sender
from users_sort import profile
bot = telebot.TeleBot(key)


# Сортировка пользователей по их действиям
@bot.message_handler(content_types=['text'])
def sorting_users(msg):
    users_sorting(bot, msg)


# Если пользователь отправил стикер пишем ему ответочку
@bot.message_handler(content_types=['sticker'])
def anti_sticker(msg):
    bot.send_message(msg.chat.id, "Каждый раз, когда вы отправляете мне стикер, в мире погибает 1 котенок(😿")


# Обработка нажатий кнопок пользователем
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    callback_op(bot, call)


@bot.message_handler(content_types=['photo'])
def photo_id(msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    photo = max(msg.photo, key=lambda x: x.height)
    try:
        res = list(cur.execute(f"SELECT place FROM history WHERE id={msg.chat.id}"))[0][0]
        if "send" in res:
            print(res)
            pic_sender(list(cur.execute(f"SELECT login FROM users WHERE player_id={msg.chat.id}"))[0],
                       int(res.split()[-1]), photo.file_id, bot, profile, msg)

    except IndexError:
        register(bot, msg)


# Зацикливание бота
bot.polling(none_stop=True, interval=1)
