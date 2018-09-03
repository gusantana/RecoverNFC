import re

class Pagamento:
	def __init__(self):
		self.dados = {}
		self.dados['Forma de Pagamento'] = { 'forma_pagamento' : '' }
		self.dados['Valor do Pagamento'] = { 'pagamento' : '' }
		self.dados['Tipo de Integração Pagamento'] = { 'tipo_integracao_pagamento' : '' }
		self.dados['CNPJ da Credenciadora'] = { 'cnpj_credenciadora' : '' }
		self.dados['Bandeira da operadora'] = { 'bandeira_operadora' : '' }
		self.dados['Número de autorização'] = { 'numero_autorizacao' : ''}

	def add(self, label, dados):
		label = label.replace("\n", '')
		label = label.strip()

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