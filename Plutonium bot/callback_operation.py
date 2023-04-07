import sqlite3
from telebot import types


def msg_sender(user1_name, user2, msg, bot, profile):
    bot.send_message(user2, f"{user1_name[0]} : {msg.text}")
    print(msg.text)
    bot.send_message(msg.chat.id, "Отправлено!")
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    cur.execute(f"UPDATE history SET place='pass' WHERE id={msg.chat.id}")
    con.commit()
    profile(msg, bot)


# Обработка нажатий на кнопки
def callback_op(bot, call):
    con = sqlite3.connect("DataBase.db")
    cur = con.cursor()
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "profile":
            role = {'user': "Гость", 'player': 'Игрок', "admin": "Админ", "moder": "Модератор", "alpha": "Альфа"}
            result = list(cur.execute(f"SELECT login, status FROM users WHERE player_id={call.message.chat.id}"))[0]
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text=f"Отмена", callback_data=f"break")
            keyboard.add(callback_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Вот ваш профиль👤\n\n📝Ваш ник: {result[0]}\n♋Ваша роль: {role[result[1]]}",
                                  reply_markup=keyboard)

        if call.data == "msg":
            result = list(cur.execute(f"SELECT login, player_id FROM users"))
            keyboard = types.InlineKeyboardMarkup()
            for i in result:
                callback_button = types.InlineKeyboardButton(text=f"{i[0]}", callback_data=f"send {i[1]}")
                keyboard.add(callback_button)
            callback_button = types.InlineKeyboardButton(text=f"Отмена", callback_data=f"break")
            keyboard.add(callback_button)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"Выберите игрока для отправки сообщения :",
                                  reply_markup=keyboard)

        if "send" in call.data:
            print(call.data)
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text=f"Отмена", callback_data=f"break")
            keyboard.add(callback_button)
            cur.execute(f"UPDATE history SET place='send {call.data.split()[-1]}' WHERE id={call.message.chat.id}")
            con.commit()
            result = list(cur.execute(f"SELECT login FROM users WHERE player_id={call.data.split()[-1]}"))[0]
            bot.send_message(call.message.chat.id, f"Напишите сообщение для {result[0]} :", reply_markup=keyboard)

        if call.data == "break":
            keyboard = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile")
            callback_button2 = types.InlineKeyboardButton(text="Мессенджер", callback_data="msg")
            keyboard.add(callback_button1)
            keyboard.add(callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="🤳Выберите действие из списка:", reply_markup=keyboard)
            con = sqlite3.connect("DataBase.db")
            cur = con.cursor()
            cur.execute(f"UPDATE history SET place='pass' WHERE id={call.message.chat.id}")
            con.commit()
    bot.answer_callback_query(call.id, "")

