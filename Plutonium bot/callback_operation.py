import sqlite3


# Обработка нажатий на кнопки
def callback_op(bot, call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "profile":
            role = {'user': "Гость", 'player': 'Игрок', "admin": "Админ", "moder": "Модератор"}
            con = sqlite3.connect("DataBase.db")
            cur = con.cursor()
            result = list(cur.execute(f"SELECT login, status FROM users WHERE player_id={call.message.chat.id}"))[0]
            bot.send_message(call.message.chat.id,
                             f"Вот ваш профиль👤\n\n📝Ваш ник: {result[0]}\n♋Ваша роль: {role[result[1]]}")

        if call.data == "msg":
            pass

    bot.answer_callback_query(call.id, "")

