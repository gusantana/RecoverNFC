import sqlite3 as database
from app.model.Item import Item
from app.model.Nota import Nota
from app.model.Empresa import Empresa
from pprint import *
class NotaBO :
	def __init__ (self, conexao):
		self.nota = Nota(conexao)
		self.item = Item(conexao)
		self.empresa = Empresa(conexao)
	
	def write(self, dados):
		try:
			pprint(dados)
			if (len(dados) > 0) :
				self.empresa.write(dados)
				self.nota.write(dados)
				self.item.write(dados)
			# if len(dados['itens']) > 0:
			# 	self.nota.write(dados)
			# 	self.item.write(dados)
			# 	print("Nota: {0} adicionada com sucesso.".format(dados['chave']))
			# else:
			# 	e = Exception("Erro na nota {0}".format(dados['url']))
			# 	raise e

		except database.IntegrityError as e:
			print("Nota: {0} já adicionada.".format(dados['chave']))

		except Exception as e:
			print(e)
		#finally:
			#pass
		
