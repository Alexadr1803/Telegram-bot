import telebot
import sqlite3
from registration import register, create_user
from bot_key import key
from telebot import types

bot = telebot.TeleBot(key)


@bot.message_handler(content_types=['text'])
def sorting_users(msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()

    try:
        res = list(cur.execute(f"SELECT place FROM history WHERE id={msg.chat.id}"))[0][0]
        if res == 'reg_name':
            create_user(bot, msg, cur, con)
        if res == 'pass':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile")
            keyboard.add(callback_button)
            bot.send_message(msg.chat.id, "Выберите действие из списка:", reply_markup=keyboard)

    except IndexError:
        register(bot, msg)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "profile":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")


bot.polling(none_stop=True, interval=1)
