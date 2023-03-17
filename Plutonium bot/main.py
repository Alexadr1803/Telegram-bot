import telebot
from pathlib import Path
import registration
import sort_user


def get_path():
    raw_path = Path(__file__).resolve()
    source_path = raw_path.parent
    return str(source_path)


bot = telebot.TeleBot('6144683206:AAGEiDwpUkZRg25pnMym5YbkvlnycuT-k-I')


@bot.message_handler()
def get_text_messages(message):
    sort_user.sort_users(message)


bot.polling(none_stop=True, interval=0)
