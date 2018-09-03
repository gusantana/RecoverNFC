import re

class Produto:
	def __init__(self):
		self.dados = {}
		self.dados['Código do Produto'] = { 'codigo' : '' }
		self.dados['Código NCM'] = { 'codigo_ncm' : '' }
		self.dados['Código CEST'] = { 'codigo_cest' : '' }
		self.dados['Código EX da TIPI'] = { 'codigo_ex_tipi' : '' }
		self.dados['CFOP'] = { 'cfop' : '' }
		self.dados['Outras Despesas Acessórias'] = { 'outras_despesas_acessorias' : ''}
		self.dados['Valor do Desconto'] = { 'valor_desconto' : '' }
		self.dados['Valor Total do Frete'] = { 'valor_frete' : '' }
		self.dados['Valor do Seguro'] = { 'valor_seguro' : '' }


	def add(self, label, dados):
		if label in self.dados:
			for i in self.dados[label]:
				dados = dados.replace("\n", '')
				dados = dados.strip() 
				self.dados[label][i] = dados

	def atualizarLista(self, lista, label):
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]

	def get(self, label):
		return self.dados[label]

	def __str__(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista.__str__()