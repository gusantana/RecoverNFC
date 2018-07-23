import sqlite3 as database

class Item :
    def __init__(self, conn):
        self.conn = conn
    
    def write(self, lista):
        sql = '''INSERT INTO item ('descricao', 'codigo', 'quantidade', 'valor') VALUES (?, ?, ?, ?)'''
        array = []
        cur = self.conn.cursor()
        for index in lista:
            item = ((lista[index]['descricao'], lista[index]['codigo'], lista[index]['quantidade'], lista[index]['valor']))
            cur.execute(sql, item)
        self.conn.commit()
        #print(array)
        #cur.executemany(sql, array)


            
