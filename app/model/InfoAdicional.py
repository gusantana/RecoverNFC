import re

class InfoAdicional:
	def __init__(self):
		self.dados = {}
		self.dados['Descrição'] = { 'descricao' : None }
		self.dados['FEDERAL'] = { 'imposto_federal' : None }
		self.dados['ESTADUAL'] = { 'imposto_estadual' : None}
		self.dados['QR-Code'] = { 'qr_code' : ''}


	def add(self, label, dados):
		label = label.replace("\n", '')
		label = label.strip()

		if 'Descrição' in label:
			lista = re.findall('[\w]+[ ]*[0-9]+[,][0-9]+', dados)
			for i in lista:
				imposto = i.split(' ')
				if imposto[0] in self.dados:
					for index in self.dados[imposto[0]]:
						self.dados[imposto[0]][index] = imposto[1]

		
		if label in self.dados:
			for i in self.dados[label]:
				dados = dados.replace("\n", '')
				dados = dados.strip()
				if dados not in '': ### necessário adicionar essa regra para evitar muitas colunas com valor '' ao invés de null
					self.dados[label][i] = dados


	def get(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista


