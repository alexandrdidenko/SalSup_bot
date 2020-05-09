from config import id_bot_and_my
from main import bot
import datetime
import os
import win32com.client as wincl


def send(my_chat_id, my_photo, my_caption, filename=__name__):
    now = datetime.datetime.now()
    dt = now.strftime("%d-%m-%Y %H:%M")
    text = my_caption + ': ' + dt
    try:
        bot.send_photo(chat_id=my_chat_id, photo=open(my_photo, 'rb'), caption=text)
    except FileNotFoundError:
        print('FileNotFoundError')
        bot.send_message(id_bot_and_my, "бот не может отправить картинку " + filename)


def run_macro(file, macros):
    if os.path.exists(file):
        print('начало работы макроса')
        excel_macro = wincl.DispatchEx("Excel.application")
        excel_macro.Visible = True  # обязательно так иначе макрос не отрабатывает
        excel_path = os.path.expanduser(file)
        workbook = excel_macro.Workbooks.Open(Filename=excel_path, ReadOnly=1)
        excel_macro.Application.Run(macros)
        # workbook.Save()
        excel_macro.Application.Quit()
        del excel_macro
        print('конец работы макроса')
    else:
        print('нет такого файла:' + file)


def del_fife(file):
    if os.path.exists(file):
        os.remove(file)
        print("фото " + file + ' удалено')
    else:
        print("The file does not exist")
