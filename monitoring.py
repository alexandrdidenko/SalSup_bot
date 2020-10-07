from time import sleep
import config
from send_sync import send_sync_my
from sql_con import sql_cursor

# условия
count_sync = 100
sleep_sec = 300


def num():
    n = 0
    res = sql_cursor(config.myServer, config.myDatabase, config.myUid, config.myPwd, config.SQL_4)

    for r in res[0]:
        n = r
    # n = 2
    return n


def chek():
    count = num()
    if count >= count_sync:
        print('норма: ' + str(count_sync) + ' - факт: ' + str(count))
        send_sync_my()
    else:
        print('норма: ' + str(count_sync) + ' - факт: ' + str(count))


i = 1
while i == 1:
    chek()
    sleep(sleep_sec)
