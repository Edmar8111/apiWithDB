import sqlite3

DATABASE='dataDB.db'

class RequestDB:
    def __init__(self, dbConn):
        self.dbConn = sqlite3.connect(DATABASE)
        self.dbConn.cursor().execute('''
            CREATE TABLE IF NOT EXISTS Container0 (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nome TEXT NOT NULL,
                                        email TEXT NOT NULL UNIQUE
                                     )
            
            ''')
        self.dbConn.row_factory=sqlite3.Row
        return None
    def closeDB(self):
        return self.dbConn.close()
    def requestGET(self):
        selectAllQuery=self.dbConn.execute('SELECT * FROM Container0').fetchall()
        dictConver=[dict(user) for user in selectAllQuery]
        return dictConver
    
    def requestPOST(self, name, email):
        self.dbConn.execute('INSERT INTO Container0 (nome, email) VALUES (?, ?)', (name, email))
        self.dbConn.commit()
        rtPOST=[dict(user) for user in self.dbConn.execute('SELECT * FROM Container0').fetchall()]
        return rtPOST