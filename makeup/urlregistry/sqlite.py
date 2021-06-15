from urllib.request import BaseHandler, urlopen
import sqlite3
import pickle
from io import BytesIO
from os import environ

SQLITE_DB = environ.get("SQLITE_DB", "sqlite.db")
ENCODING = environ.get("SQLITE_ENCODING", 'utf-8')


class SQLiteHandler(BaseHandler):
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_DB)

    def sql_open(self, req):
        schema, tail = req.full_url.split(':')
        url = 'file' + ':' + tail
        q = urlopen(url, 'rb').read().decode('utf-8')
        data = [row for row in self.conn.execute(q)]
        return BytesIO(pickle.dumps(data))
