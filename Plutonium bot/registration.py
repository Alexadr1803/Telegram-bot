import sqlite3


def create_user(bot, msg, cur, con):
    if len(msg.text) < 16:
        cur.execute(f"INSERT INTO users VALUES ({msg.chat.id}, '{msg.text}', 'user' ) ")
        con.commit()
        cur.execute(f"UPDATE history SET place='pass' WHERE id={msg.chat.id}")
        con.commit()
        bot.send_message(msg.chat.id, "Вы зарегистрированы!")
    else:
        bot.send_message(msg.chat.id, "У вас слишком длинный ник! Введите новый!")


def register(bot, msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    try:
        list(cur.execute(f"SELECT login FROM users WHERE player_id={msg.chat.id}"))[0][0]
    except IndexError:
        bot.send_message(msg.chat.id, "Вам нужно зарегистрироваться!")
        cur.execute(f"INSERT INTO history(id, place) VALUES({msg.chat.id}, 'reg_name')")
        con.commit()
        bot.send_message(msg.chat.id, "Напишите свой никнейм")
