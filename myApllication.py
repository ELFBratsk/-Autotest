import pymysql
from pymysql.connections import Connection

from config import host , user, password ,db_name




try :
    connection: Connection = pymysql.connect(
        host=host,
        port=1521,
        password = password,
        db_name = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('ok')

except Exception as ex :
    print('connect no')
    print(ex)
