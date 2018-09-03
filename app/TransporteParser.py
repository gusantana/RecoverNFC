from core.BaseParser import BaseParser
from app.model.Totais import Totais
import re

class TransporteParser (BaseParser):
	def __init__(self):
		BaseParser.__init__(self)
		self.dados = {}

		self.tag_label = ('label')
		self.tag_dados = ('span')

		self.gravar_label = False
		self.gravar_dados = False
	
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
			#self.totais.add(self.ultima_label, data)
			#self.dados#
			pass


	def __str__(self):
		return this.totais.__str__()