import re
#from app.model.Empresa import Empresa
from html import parser
from app.model.InfoAdicional import InfoAdicional

class InfoAdicionalParser(parser.HTMLParser):
	def __init__(self):
		parser.HTMLParser.__init__(self)
		self.tag_label = ('label')
		self.tag_dados = ('span')

		self.gravar_dados = False
		self.gravar_label = False
		self.ultima_label = ""
		self.info_adicional = InfoAdicional()

	def handle_starttag(self, tag, atributos):
		if tag in self.tag_label:
			self.gravar_label = True
		if tag in self.tag_dados:
			self.gravar_dados = True

	def handle_endtag(self, tag):
		if tag in self.tag_label:
			self.gravar_label = False
		if tag in self.tag_dados:
			self.gravar_dados = False


	def handle_data(self, data):
		if self.gravar_label:
			self.ultima_label = data
		if self.gravar_dados:
			self.info_adicional.add(self.ultima_label, data)
	
	def get(self):
		return self.info_adicional.get()