#Parser correspondente da aba NFCe
from pprint import *
from html import parser
import re
from app.model.NFCe import *

class NFCeParser(parser.HTMLParser):
	def __init__(self):
		parser.HTMLParser.__init__(self)
		self.tags_tabela = ('td')
		self.gravarLabel = False
		self.gravarDados = False
		self.dados = []
		self.nfce = NFCe()
		self.ultima_label = ""


	def handle_starttag(self, tag, atributos):
		if tag in self.tags_tabela:
			self.gravarDados = True
			self.gravarLabel = True

	def handle_endtag(self, tag):
		if tag in self.tags_tabela:
			self.gravarDados = False
			self.gravarLabel = False
		

	def handle_data(self, data):
		if self.gravarDados:
			if self.gravarLabel:
				self.gravarLabel = False
				self.ultima_label = data
				return
			self.nfce.add(self.ultima_label, data)
			
	def __str__(self):
		return self.nfce.__str__()
