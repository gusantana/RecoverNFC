import sqlite3 as database
from pprint import *
class Nota :
	'''
	SQL CREATE:
	CREATE TABLE "nota" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `chave` TEXT NOT NULL UNIQUE, `chave_str` TEXT, `data_hora` TEXT, `data_cadastro` TEXT NOT NULL )
	'''

	def __init__(self, conn):
		self.conn = conn

	def write(self, lista):#recebe a lista já parseada
		try:
			comum = lista['comum']
			nfce = lista['nfce']
			id_empresa = lista['empresa']['id']

			sql = '''INSERT INTO nota (
						id_empresa,
						chave,
						chave_str,
						data_hora, 
						finalidade, 
						forma_pagamento, 
						natureza_operacao, 
						modelo, 
						numero,
						serie,
						tipo_emissao,
						tipo_operacao,
						versao_processo,
						data_cadastro)
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime(datetime(), "-240 minutes")'''

			param = (id_empresa, comum['chave'], comum['chave_str'], chave['data_hora'], nfce['finalidade'], nfce['fomra_pagamento'], nfce['natureza_operacao'], nfce['modelo'], nfce['numero'], nfce['serie'], nfce['tipo_emissao'], nfce['tipo_operacao'], nfce['versao_processo'])

			cur.execute(sql, param)
			# if not 'data_hora' in lista:
			# 	lista['data_hora'] = 'EM CONTINGENCIA'
			# sql = '''INSERT INTO nota ('chave', 'chave_str', 'data_hora', 'data_cadastro') VALUES (?, ?, ?, datetime(datetime(), "-240 minutes")) '''
			# cur = self.conn.cursor()
			# row = (lista['chave'], lista['chave_str'], lista['data_hora'])

			# cur.execute(sql, row)

			# cur = self.conn.cursor()
			cur.execute("SELECT last_insert_rowid()")
			id_nota = cur.fetchone()[0]
			lista['nfce']['id'] = id_nota
			# lista['nota_id'] = nota_id

		except Exception as e:
			raise e
		#finally:
			#pass