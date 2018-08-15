import sqlite3 as database

class Nota :
	'''
	SQL CREATE:
	CREATE TABLE "nota" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `chave` TEXT NOT NULL UNIQUE, `chave_str` TEXT, `data_hora` TEXT, `data_cadastro` TEXT NOT NULL )
	'''

	def __init__(self, conn):
		self.conn = conn

	def write(self, lista):#recebe a lista já parseada
		#print(lista)
		#
		sql = '''INSERT INTO nota ('chave', 'chave_str', 'data_hora', 'data_cadastro') VALUES (?, ?, ?, datetime(datetime(), "-240 minutes")) '''
		cur = self.conn.cursor()
		row = (lista['chave'], lista['chave_str'], lista['data_hora'])
		print(row)
		#cur.execute(sql, row)
		#self.conn.commit()

		cur = self.conn.cursor()
		cur.execute("SELECT last_insert_rowid()")
		nota_id = cur.fetchone()[0]
		lista['nota_id'] = nota_id
		return lista