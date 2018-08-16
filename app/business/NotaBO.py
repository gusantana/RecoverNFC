import sqlite3 as database
from app.model.Item import Item
from app.model.Nota import Nota

class NotaBO :
	def __init__ (self, conexao):
		self.nota = Nota(conexao)
		self.item = Item(conexao)
	
	def write(self, dados):
		try:
			if (len(dados['itens']) > 0):
				dados = self.nota.write(dados)
				self.item.write(dados)

		except Exception as e:
			print(e)
		finally:
			pass
		
