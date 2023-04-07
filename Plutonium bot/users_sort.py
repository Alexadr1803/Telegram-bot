import sqlite3
from registration import register, create_user
from telebot import types
from callback_operation import msg_sender


def profile(msg, bot):
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile")
    callback_button2 = types.InlineKeyboardButton(text="Мессенджер", callback_data="msg")
    keyboard.add(callback_button1)
    keyboard.add(callback_button2)
    bot.send_message(msg.chat.id, "🤳Выберите действие из списка:", reply_markup=keyboard)


# Функция сортирующая запросы пользователей по их статусам
def users_sorting(bot, msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()

    try:
        res = list(cur.execute(f"SELECT place FROM history WHERE id={msg.chat.id}"))[0][0]
        if res == 'reg_name':
            create_user(bot, msg, cur, con)

        if res == 'pass':
            profile(msg, bot)

        if "send" in res:
            print(res)
            msg_sender(list(cur.execute(f"SELECT login FROM users WHERE player_id={msg.chat.id}"))[0],
                       int(res.split()[-1]), msg, bot, profile)

    except IndexError:
        register(bot, msg)
