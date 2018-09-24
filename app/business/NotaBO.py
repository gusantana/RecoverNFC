import sqlite3 as database
from app.model.Produto import Produto
from app.model.Nota import Nota
from app.model.Empresa import Empresa
from app.model.Totais import Totais
from app.model.Pagamento import Pagamento
from app.model.InfoAdicional import InfoAdicional
from pprint import *
class NotaBO :
	def __init__ (self, conexao):
		self.empresa = Empresa(conexao)
		self.nota = Nota(conexao)
		# self.item = Item(conexao)
		self.produto = Produto(conexao)
		self.pagamento = Pagamento(conexao)
		self.totais = Totais(conexao)
		self.info_adicional = 
		self.conexao = conexao
	
	def write(self, dados):
		try:
			if (len(dados) > 0) :
				self.empresa.write(dados)
				self.nota.write(dados)
				self.produto.write(dados)
				self.totais.write(dados)
				self.pagamento.write(dados)
				self.info_adicional.write(dados)
				self.conexao.commit()
			# if len(dados['itens']) > 0:
			# 	self.nota.write(dados)
			# 	self.item.write(dados)
				print("Nota: {0} adicionada com sucesso.".format(dados['comum']['chave']))
			# else:
			# 	e = Exception("Erro na nota {0}".format(dados['url']))
			# 	raise e

		except database.IntegrityError as e:
			print("Nota: {0} já adicionada.".format(dados['comum']['chave']))

		except Exception as e:
			print(e)
		#finally:
			#pass
		
