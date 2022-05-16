from .DB import DB


class Query(DB):
    def __init__(self, db_type):
        super(Query, self).__init__(db_type)

    def createTables(self, tableName: str, columns: list):
        try:
            data = ','.join(str(elem) for elem in columns)
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {tableName} ({data})")

        except:
            print('The table was not created')

        self.db.commit()

        return self

    def insert(self, tableName: str, values: dict):
        try:
            keys = ','.join(str("`" + elem + "`") for elem in values.keys())
            values = ','.join(str("'" + elem + "'") for elem in values.values())
            self.conn.execute(f"INSERT INTO {tableName}({keys}) VALUES ({values})")

            self.db.commit()
        except TypeError:
            print(f'The data was not inserted {TypeError}')
        return self

    def dropTable(self, tableName: str):
        try:
            self.conn.execute(f"DROP TABLE IF EXISTS {tableName}")

            self.db.commit()
        except Exception:
            print(Exception)
        return self