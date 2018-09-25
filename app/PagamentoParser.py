from app.model.Pagamento import Pagamento
from core.BaseParser import BaseParser

class PagamentoParser (BaseParser):
	def __init__(self):
		BaseParser.__init__(self)
		self.tags_validos = ('span')
		self.gravar_dados = False
		self.cur_item = 0
		self.pagamento = Pagamento()

	def handle_starttag(self, tag, atributos):
		#print (tag)
		if tag in self.tags_validos:
			self.gravar_dados = True
		

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		if self.gravar_dados:
			self.pagamento.add(self.cur_item, data)
			self.gravar_dados = False
			self.cur_item += 1

	def get(self):
		return self.pagamento.get()

