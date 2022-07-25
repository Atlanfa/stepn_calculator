import time

import telebot
from KEY import key
from get_curent_price import get_GST

from keyboard import main_reply_keyboard

API_TOKEN = key

bot = telebot.TeleBot(API_TOKEN)

currency = {'gst_current': 0.0, 'gst_needed': 0.0, 'chat_id': 0, 'state': '','break': 0}


@bot.message_handler(commands=['start'])
def start_message(message):
    currency['chat_id'] = message.chat.id
    bot.send_message(currency['chat_id'], f"Добро пожаловать {message.from_user.first_name}", reply_markup=main_reply_keyboard())


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'Текущий курс':
        currency['gst_current'] = get_GST()
        bot.send_message(currency['chat_id'], f"Сейчас курс gst такой - {currency['gst_current']}")
    elif message.text == 'Установить курс':
        currency['state'] = 'Установить курс'
    elif currency['state'] == 'Установить курс':
        try:
            value = float(message.text)
            currency['gst_needed'] = value
            currency['state'] = ''
            while True:
                try:
                    if currency["break"] == 1:
                        currency['break'] = 0
                        break
                    currency['gst_current'] = get_GST()
                    if currency['gst_current'] > currency['gst_needed']:
                        bot.send_message(currency['chat_id'],
                                         f'Сейчас gst = {currency["gst_current"]}$, вы хотели проверить не больше ли он чем {currency["gst_needed"]}')

                    time.sleep(10) #15 min = 900

                except:
                    break
        except:
            bot.send_message(currency['chat_id'], 'Введите число в формате 10.10')
    elif message.text == 'Стоп':
        currency['break'] = 1
        currency['state'] = ''


@bot.message_handler(commands=['setCurrencyValueGST', 'stop'])
def set_currency(message):
    value = float(message.text.split(' ')[-1])
    currency['gst_needed'] = value
    currency['gst_current'] = get_GST()
    bot.send_message(currency['chat_id'], f"Сейчас курс gst такой - {currency['gst_current']}")
    while True:
        try:
            if message.text == '/stop':
                break
            currency['gst_current'] = get_GST()
            if currency['gst_current'] > currency['gst_needed']:
                bot.send_message(currency['chat_id'],
                                 f'Сейчас gst = {currency["gst_current"]}$, вы хотели проверить не больше ли он чем {currency["gst_needed"]}')

            time.sleep(10)
        except:
            break


def check_if_greater_gst():
    currency['gst_current'] = get_GST()
    if currency['gst_current'] < currency['gst_needed']:
        bot.send_message(currency['chat_id'], f'Сейчас gst = {currency["gst_current"]}$, вы хотели проверить не больше ли он чем {currency["gst_needed"]}')

bot.infinity_polling()
