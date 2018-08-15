import sqlite3 as database

class Item :
    '''
    SQL CREATE:
    CREATE TABLE "item" ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `nota_id` INTEGER NOT NULL, `descricao` TEXT NOT NULL, `codigo` INTEGER, `quantidade` REAL NOT NULL, `valor` REAL NOT NULL, FOREIGN KEY(`nota_id`) REFERENCES `nota`(`id`) ON UPDATE CASCADE ON DELETE CASCADE )
    '''
    def __init__(self, conn):
        self.conn = conn
    
    def write(self, lista):
        print(lista)
        sql = '''INSERT INTO item ('descricao', 'nota_id', 'codigo', 'quantidade', 'valor') VALUES (?, ?, ?, ?, ?)'''
        cur = self.conn.cursor()
        nota_id = lista['nota_id']
        
        print(nota_id)
        for index in lista:
            print(index)
            item = ((lista[index]['descricao'], nota_id, lista[index]['codigo'], lista[index]['quantidade'], lista[index]['valor']))
            #print(lista['nota_id'])
            #cur.execute(sql, item)
        #self.conn.commit()



            
