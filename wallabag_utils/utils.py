import json
import os
import sqlite3 as lite

DB_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE_DB = '{}/tmp/poche.sqlite'.format(DB_PATH)

queries = [
    {'sql': 'SELECT id, title, url FROM entries',
     'file': 'entries.json'},
    {'sql': 'SELECT id, value FROM tags',
     'file': 'tags.json'},
    {'sql': 'SELECT entry_id, tag_id FROM tags_entries',
     'file': 'tags_entries.json'}
]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


try:
    connection = lite.connect(SQLITE_DB)
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query['sql'])
        file_name = '{}/tmp/{}'.format(DB_PATH, query['file'])
        with open(file_name, 'w') as output_file:
            output_file.write(json.dumps(cursor.fetchall()))

except Exception as e:
    print('Exception: {}'.format(e.message))
finally:
    if connection:
        connection.close()
