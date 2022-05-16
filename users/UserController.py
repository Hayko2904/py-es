from database.Query import Query
import bcrypt

class UserController:
    def __init__(self):
        self.db = Query('sqlite')
        self.db.createTables("users", [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "email TEXT NOT NULL UNIQUE",
            "password TEXT NOT NULL"
        ])

    def login(self, data: dict) -> bool:
        user = self.db.conn.execute(f"SELECT * FROM users WHERE email = '{data['email']}'").fetchone()
        if bcrypt.checkpw(data['password'].encode('utf-8'), user['password'].encode('utf-8')):
            return True

        return False

    def registration(self, data: dict) -> bool:
        conn = self.db
        data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        conn.insert("users", data).close()

        return True

    def __del__(self):
        self.db.close()

