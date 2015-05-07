__author__ = 'ekalyoncu'

import mysql.connector
import traceback

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root123'
MYSQL_HOST = 'localhost'
MYSQL_DB = 'abc'


def within_conn(block):
    cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB, host=MYSQL_HOST)
    cursor = cnx.cursor()
    try:
        result = block(cnx, cursor)
        cnx.commit()
        return result
    except Exception, err:
        cnx.rollback()
        print traceback.format_exc()
        raise err
    finally:
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()