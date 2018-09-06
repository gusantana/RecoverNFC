import re

class Pagamento:
	def __init__(self):
		# self.dados = {}
		self.dados = []
		self.dados.append({ 'forma_pagamento' : ''})
		self.dados.append({ 'pagamento' : '' })
		self.dados.append({ 'tipo_integracao_pagamento' : '' })
		self.dados.append({ 'cnpj_credenciadora' : '' })
		self.dados.append({ 'bandeira_operadora' : '' })
		self.dados.append({ 'numero_autorizacao' : ''})

	def add(self, index, valor):
		valor = valor.replace('\n', '')
		valor = valor.strip()
		valor = re.sub('^[0-9]+\s+-\s+', '', valor)
		for label in self.dados[index]:
			self.dados[index][label] = valor

	def get(self):
		dados = {}
		for valores in self.dados:
			for coluna in valores:
				dados[coluna] = valores[coluna]
		return dados

	def __str__(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista.__str__()