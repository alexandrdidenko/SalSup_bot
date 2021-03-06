# coding:utf-8
import config
import requests
import telebot
import pythoncom
import keyboards as kb
import send_cube_sales
import send_dd_chek
import send_infochek
import send_prim_sec_sales
import send_sync
import send_sync_count
import task
import send_export
import send_poc_ka

URL = 'https://api.telegram.org/bot' + config.TOKEN + '/'
bot = telebot.TeleBot(config.TOKEN)


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


@bot.message_handler(commands=["start"])
def start(message):
    task.log(message)
    bot.send_message(message.chat.id, "Choose one comand:", reply_markup=kb.markup)


@bot.message_handler(commands=["infocheck"])
def infocheck(message):
    pythoncom.CoInitialize()
    task.log(message)
    # task.run_macro(config.xls_infoChek, config.macros_infoChek)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_infoChek, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_infoChek)
    send_infochek.infochek(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["cube_sales"])
def cube_sales(message):
    pythoncom.CoInitialize()
    task.log(message)
    # task.run_macro(config.xls_cube_sales, config.macros_cube_sales)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_cube_sales, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_cube_sales)
    send_cube_sales.cube_sales(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["prim_sec_sales"])
def prim_sec_sales(message):
    pythoncom.CoInitialize()
    task.log(message)
    # task.run_macro(config.xls_prim_sec_sales, config.macros_prim_sec_sales)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_prim_sec_sales, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_prim_sec_sales)
    send_prim_sec_sales.prim_sec_sales(prim_sec_sales)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["sync"])
def planing(message):
    pythoncom.CoInitialize()
    # старый текст для работы бота. Переделал на работу через функцию
    # task.log(message)
    # task.run_macro(config.xls_sync, config.macros_sync)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_sync, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_sync)
    task.log(message)
    send_sync.sync(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["export"])
def planing(message):
    pythoncom.CoInitialize()
    task.log(message)
    # старый текст для работы бота. Переделал на работу через функцию
    # task.run_macro(config.xls_export, config.macros_export)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_export, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_export)
    send_export.export(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["DD_chek"])
def planing(message):
    pythoncom.CoInitialize()
    task.log(message)
    # task.run_macro(config.xls_DD_chek, config.macros_DD_chek)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_DD_chek, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_DD_chek)
    send_dd_chek.dd_chek(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["sync_count"])
def planing(message):
    pythoncom.CoInitialize()
    task.log(message)
    # task.run_macro(config.xls_sync_count, config.macros_sync_count)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_sync_count, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_sync_count)
    send_sync_count.sync_count(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["poc_ka"])
def planing(message):
    pythoncom.CoInitialize()
    task.log(message)
    # task.run_macro(config.xls_sync_count, config.macros_sync_count)
    # try:
    #     bot.send_photo(chat_id=message.chat.id,
    #                    photo=open(config.photo_sync_count, 'rb'))
    # except FileNotFoundError:
    #     print('FileNotFoundError')
    #     bot.send_message(message.chat.id, "нет изображения", reply_markup=kb.markup)
    #
    # task.del_fife(config.photo_sync_count)
    send_poc_ka.poc_ka(message.chat.id)
    pythoncom.CoUninitialize()


@bot.message_handler(commands=["test"])
def planing(message):
    pythoncom.CoInitialize()
    # send_sync.send_sync(message.chat.id)
    pythoncom.CoUninitialize()


if __name__ == '__main__':
    print("бот стартонул. Ждет команду")
    bot.polling(none_stop=True, interval=0)
