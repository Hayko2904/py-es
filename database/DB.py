import sqlite3

import mysql.connector
from decouple import config


class DB:
    def __init__(self, db_type):
        if db_type == 'sqlite':
            self.db = sqlite3.connect("./../db.db", timeout=10)
            self.db.row_factory = sqlite3.Row
        else:
            self.db = mysql.connector.connect(
                host=config('MYSQL_HOST'),
                port=config('MYSQL_PORT'),
                user=config('MYSQL_USER'),
                password=config('MYSQL_PASSWORD'),
                database=config('MYSQL_DB')
            )

        self.conn = self.db.cursor()

    def close(self):
        self.conn.close()
