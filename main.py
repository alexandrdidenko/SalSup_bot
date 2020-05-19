# coding:utf-8
import config
import requests
import telebot
# import sql_con
import pythoncom
import keyboards as kb
import task

URL = 'https://api.telegram.org/bot' + config.TOKEN + '/'
bot = telebot.TeleBot(config.TOKEN)

print("бот стартонул. Ждет команду")


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Choose one comand:", reply_markup=kb.markup)


@bot.message_handler(commands=["infocheck"])
def infocheck(message):
    pythoncom.CoInitialize()
    task.run_macro(config.xls_infoChek, config.macros_infoChek)
    try:
        bot.send_photo(chat_id=message.chat.id,
                       photo=open(config.photo_infoChek, 'rb'))
        print(message.text)
    except FileNotFoundError:
        print('FileNotFoundError')
        bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)

    task.del_fife(config.photo_infoChek)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["cube_sales"])
def cube_sales(message):
    pythoncom.CoInitialize()
    task.run_macro(config.xls_cube_sales, config.macros_cube_sales)
    try:
        bot.send_photo(chat_id=message.chat.id,
                       photo=open(config.photo_cube_sales, 'rb'))
        print(message.text)
    except FileNotFoundError:
        print('FileNotFoundError')
        bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)

    task.del_fife(config.photo_cube_sales)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["prim_sec_sales"])
def prim_sec_sales(message):
    pythoncom.CoInitialize()
    task.run_macro(config.xls_prim_sec_sales, config.macros_prim_sec_sales)
    try:
        bot.send_photo(chat_id=message.chat.id,
                       photo=open(config.photo_prim_sec_sales, 'rb'))
        print(message.text)
    except FileNotFoundError:
        print('FileNotFoundError')
        bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)

    task.del_fife(config.photo_prim_sec_sales)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["sync"])
def planing(message):
    pythoncom.CoInitialize()
    task.run_macro(config.xls_sync, config.macros_sync)
    try:
        bot.send_photo(chat_id=message.chat.id,
                       photo=open(config.photo_sync, 'rb'))
        print(message.text)
        # print(message.chat.id)
    except FileNotFoundError:
        print('FileNotFoundError')
        bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)

    task.del_fife(config.photo_sync)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["export"])
def planing(message):
    pythoncom.CoInitialize()
    task.run_macro(config.xls_export, config.macros_export)
    try:
        bot.send_photo(chat_id=message.chat.id,
                       photo=open(config.photo_export, 'rb'))
        print(message.text)
        # print(message.chat.id)
    except FileNotFoundError:
        print('FileNotFoundError')
        bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)

    task.del_fife(config.photo_export)
    pythoncom.CoUninitialize()


#
# @bot.message_handler(commands=["test"])
# def start(message):
#     mess = sql_con.sql_cursor(config.myServer, config.myDatabase, config.myUid, config.myPwd, config.SQL_2)
#     bot.send_message(message.chat.id, mess, reply_markup=markup)
#     print(mess)


if __name__ == '__main__':
    bot.polling(none_stop=True)
