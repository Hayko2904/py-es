from .DB import DB


class Query(DB):
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
            self.conn.execute(f"insert into {tableName} ({keys}) values ({values})")

            self.db.commit()
        except:
            print('The data was not inserted')
        return self
