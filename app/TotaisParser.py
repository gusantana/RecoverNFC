from core.BaseParser import BaseParser
from app.model.Totais import Totais
import re

class TotaisParser (BaseParser):
	def __init__(self):
		BaseParser.__init__(self)
		self.dados = {}
		#self.dados['']
		#self.tags_validos = ('label', 'span')
		self.tag_label = ('label')
		self.tag_dados = ('span')
		self.gravar_label = False
		self.gravar_dados = False
		self.totais = Totais()

	
	def handle_starttag(self, tag, atributos):
		if tag in self.tag_label:
			self.gravar_label = True
			return
		if tag in self.tag_dados:
			self.gravar_dados = True
	
	def handle_endtag(self, tag):
		if tag in self.tag_label:
			self.gravar_label = False
		if tag in self.tag_dados:
			self.grava_dados = False

	def handle_data(self, data):
		if self.gravar_label:
			self.ultima_label = data
			return
		if self.gravar_dados:
			self.totais.add(self.ultima_label, data)


	def __str__(self):
		return this.totais.__str__()

	def get(self):
		return self.totais.get()
		#lista = {}
		#for label in self.dados:
			#for i in self.dados[label]:
				#lista[i] = self.dados[label][i]
		#return lista.__str__()