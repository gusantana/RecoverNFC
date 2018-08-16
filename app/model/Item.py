import sqlite3 as database

class Item :
    '''
    SQL CREATE:
    CREATE TABLE "item" ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `nota_id` INTEGER NOT NULL, `descricao` TEXT NOT NULL, `codigo` INTEGER, `quantidade` REAL NOT NULL, `valor` REAL NOT NULL, FOREIGN KEY(`nota_id`) REFERENCES `nota`(`id`) ON UPDATE CASCADE ON DELETE CASCADE )
    '''
    def __init__(self, conn):
        self.conn = conn
    
    def write(self, lista):
        try:
            sql = '''INSERT INTO item ('descricao', 'nota_id', 'codigo', 'quantidade', 'valor') VALUES (?, ?, ?, ?, ?)'''
            cur = self.conn.cursor()
            nota_id = lista['nota_id']

            for index in lista['itens']:
                item = ((lista['itens'][index]['descricao'], nota_id, lista['itens'][index]['codigo'], lista['itens'][index]['quantidade'], lista['itens'][index]['valor']))
                #print(lista['nota_id'])
                cur.execute(sql, item)
            self.conn.commit()
        except Exception as e:
            raise e
        



            

