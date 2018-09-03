from app.model.Pagamento import Pagamento
from core.BaseParser import BaseParser

class PagamentoParser (BaseParser):
	def __init__(self):
		BaseParser.__init__(self)
		self.dados = {}

	def handle_starttag(self, tag, atributos):
		print (tag)
		

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		print(data)
		

