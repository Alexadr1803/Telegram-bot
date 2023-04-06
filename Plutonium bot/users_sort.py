import sqlite3
from registration import register, create_user
from telebot import types


def users_sort(bot, msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()

    try:
        res = list(cur.execute(f"SELECT place FROM history WHERE id={msg.chat.id}"))[0][0]
        if res == 'reg_name':
            create_user(bot, msg, cur, con)
        if res == 'pass':
            keyboard = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile")
            callback_button2 = types.InlineKeyboardButton(text="Мессенджер", callback_data="msg")
            keyboard.add(callback_button1)
            keyboard.add(callback_button2)
            bot.send_message(msg.chat.id, "🤳Выберите действие из списка:", reply_markup=keyboard)

    except IndexError:
        register(bot, msg)
