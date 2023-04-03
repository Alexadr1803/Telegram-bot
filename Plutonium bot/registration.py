import telebot
import sqlite3


def register(bot, msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    try:
        result = list(cur.execute(f"SELECT login FROM users WHERE id={msg.chat.id}"))[0][0]

    except IndexError:
        bot.send_message(msg.chat.id, "Вам нужно зарегистрироваться!")
        cur.execute(f"INSERT INTO history(id, place) VALUES({msg.chat.id}, 'reg_name')")
        con.commit()
        bot.send_message(msg.chat.id, "Напишите свой никнейм")
