#Parser correspondente da aba NFCe
from pprint import *
from html import parser
import re
from app.model.Empresa import Empresa

class EmitenteParser(parser.HTMLParser):
	def __init__(self):
		parser.HTMLParser.__init__(self)
		self.tags_tabela = ('td')
		self.tags_label = ('span')
		self.gravarDados = False
		self.gravarLabel = False
		self.ultima_label = ""
		self.empresa = Empresa()

	def handle_starttag(self, tag, atributos):
		if tag in self.tags_label:
			self.gravarDados = True
			return
		if tag in self.tags_tabela:
			self.gravarLabel = True
		

	def handle_endtag(self,tag):
		if tag in self.tags_tabela:
			self.gravarDados = False
			self.gravarLabel = False

	def handle_data(self, data):
		if self.gravarLabel:
			self.gravarLabel = False
			self.ultima_label = data
			return
		if self.gravarDados:
			self.empresa.add(self.ultima_label, data)
			self.gravarDados = False

	def __str__(self):
		return self.empresa.__str__()