from time import sleep
import config
from send_sync import send_sync_my
from sql_con import sql_cursor

# условия
count_sync1 = 50
count_sync2 = 20
sleep_sec = 300

lim = count_sync1


def num():
    n = 0
    res = sql_cursor(config.myServer, config.myDatabase, config.myUid, config.myPwd, config.SQL_4)

    for r in res[0]:
        n = r
    # n = 19
    return n


def chek(sync1, sync2):
    count = num()
    global lim
    try:
        if count >= lim:
            lim = sync2
            print('норма:', lim, ' - факт:', count)
            print('отправляем статус')
            send_sync_my()
        else:
            lim = sync1
            print('норма:', lim, ' - факт:', count)
    except TypeError:
        print('проверь ВПН. нет связи с сервером')


i = 1
while i == 1:
    chek(count_sync1, count_sync2)
    sleep(sleep_sec)
