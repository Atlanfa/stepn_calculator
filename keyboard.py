from telebot import types


def main_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    btn_current = types.KeyboardButton('Текущий курс')
    btn_new = types.KeyboardButton('Установить курс')
    btn_stop = types.KeyboardButton('Стоп')
    markup.add(btn_current, btn_new, btn_stop)
    return markup
