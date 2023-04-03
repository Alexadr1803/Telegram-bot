import telebot
import sqlite3
from registration import register
bot = telebot.TeleBot('6144683206:AAGEiDwpUkZRg25pnMym5YbkvlnycuT-k-I')


@bot.message_handler(content_types=['text'])
def sorting_users(msg):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    try:
        res = list(cur.execute(f"SELECT place FROM history WHERE id={msg.chat.id}"))[0][0]
        if res == 'reg_name':
            # регистрация никнейма игрока
            if len(msg.text) < 16:
                cur.execute(f"INSERT INTO users(id, status, login) VALUES({msg.chat.id}, 'user', {msg.text})")
                con.commit()
                bot.send_message(msg.chat.id, "Вы зарегистрированы!")
            else:
                bot.send_message(msg.chat.id, "У вас слишком длинный ник! Введите новый!")
    except IndexError:
        register(bot, msg)


bot.polling(none_stop=True, interval=0)
