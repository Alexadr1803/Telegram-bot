from telegram.ext import CommandHandler  # импортируем нужные билиотеки


async def start(update, context):  # ответ на команду /start
    user = update.effective_user  # user - переменная с данными о пользователе
    await update.message.reply_html(  # ответ на сообщение
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    )  # конец функции.


async def help_command(update, context):  # ответ на команду /help
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")  # ответ бота со всеми
    # возможными функциями
    # конец функции.

async def login(update, context):  # TODO функция для ввхода в систему под именем
    pass

async def post_news(update, context): # TODO функция для создания новостей
    pass

async def (update, context):

def main():  # функция main - функция для создания объектов обробатоки
    application = Application.builder().token("").build()  # Создаём объект Application

     # Создаём обработчик сообщений типа filters.TEXT
     # из описанной выше асинхронной функции echo()
     # После регистрации обработчика в приложении
     # эта асинхронная функция будет вызываться при получении сообщения
     # с типом "текст", т. е. текстовых сообщений.
     text_handler = MessageHandler(filters.TEXT, echo)

    # Регистрируем обработчик в приложении.
    application.add_handler(text_handler)

    # Запускаем приложение.
    application.run_polling()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
