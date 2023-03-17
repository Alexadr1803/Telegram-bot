import registration
import telebot
import sqlite3


def sort_users(message):
    con = sqlite3.connect("users_info.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM users
                WHERE chat_id = {message.chat.id}""").fetchall()
    print(message.chat.id)
    if result is []:
        registration.reg()
    con.close()
