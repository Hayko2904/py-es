import mysql.connector
from decouple import config


class DB:
    def __init__(self):
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
