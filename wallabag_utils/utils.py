import sqlite3 as lite

import os

DB_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE_DB = '{}/tmp/poche.sqlite'.format(DB_PATH)

try:
    connection = lite.connect(SQLITE_DB)
    cursor = connection.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchall()
    print('RESULTSET: {}'.format(repr(data)))
except Exception as e:
    print('Exception: {}'.format(e.message))
finally:
    if connection:
        connection.close()
