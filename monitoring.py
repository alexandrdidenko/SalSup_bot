import datetime
import os
from time import sleep
import config
import send_sync
from sql_con import sql_cursor

# условия
count_sync1 = 80
count_sync2 = 30
sleep_sec1 = 900
sleep_sec2 = 300

lim = count_sync1
sec = sleep_sec1


def num():
    n = 0
    res = sql_cursor(config.myServer, config.myDatabase, config.myUid, config.myPwd, config.SQL_4)

    for r in res[0]:
        n = r
    # n = 19
    return n


def chek(sync1, sync2, sleep1, sleep2):
    count = num()
    global lim
    global sec
    now = datetime.datetime.now()
    try:
        if count >= lim:
            lim = sync2
            sec = sleep2
            print(now.strftime("%d-%m-%Y %H:%M"), 'норма:', lim, 'факт:', count, 'ждем:', sec, 'секунд')
            print('отправляем статус')
            send_sync.sync(config.ID_SALESSUPPORT_CHANNEL)
            # send_sync.sync(config.id_bot_and_my)
        else:
            lim = sync1
            sec = sleep1
            print(now.strftime("%d-%m-%Y %H:%M"), 'норма:', lim, 'факт:', count, 'ждем:', sec, 'секунд')
    except TypeError:
        print('проверь ВПН. нет связи с сервером')
        os.system(r'C:\Users\alexandr.didenko\Desktop\VPN-on.bat')


i = 1
while i == 1:
    chek(count_sync1, count_sync2, sleep_sec1, sleep_sec2)
    #sleep(sec)

    a = sec
    while a > 0:
    	print(a)
    	a = a-1
    	sleep(1)