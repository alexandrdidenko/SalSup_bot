import pypyodbc
import config

from datetime import datetime
import time


def sql_cursor(myServer, myDatabase, myUid, myPwd, sql):
    connection_string = 'Driver={SQL Server Native Client 11.0};Server=%s;Database=%s;Uid=%s;Pwd=%s;' % (
        myServer, myDatabase, myUid, myPwd)
    try:
        connection = pypyodbc.connect(connection_string)
        cur = connection.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        connection.close()
        print('соединение закрыто')
    except:
        print("Error: unable to fetch data")
        res = "Error: unable to fetch data"

    return res
