import re

class Totais:
	def __init__(self):
		self.dados = {}
		self.dados['Base de Cálculo ICMS'] = { 'base_icms' : None }
		self.dados['Valor do ICMS'] = { 'valor_icms' : None }
		self.dados['Valor do ICMS Desonerado'] = { 'icms_desonerado' : None }
		self.dados['Base de Cálculo ICMS ST'] = { 'base_icms_st' : None }
		self.dados['Valor ICMS Substituição'] = { 'icms_substituicao' : None }
		self.dados['Valor Total dos Produtos'] = { 'valor_total_produtos' : None}
		self.dados['Valor do Frete'] = { 'frete' : None }
		self.dados['Valor do Seguro'] = { 'seguro' : None }
		self.dados['Outras Despesas Acessórias'] = { 'outras_despesas_acessorias' : None }
		self.dados['Valor Total do IPI'] = { 'total_ipi' : None }
		self.dados['Valor Total da NFe'] = { 'total_nfe' : None }
		self.dados['Valor Total dos Descontos'] = { 'total_descontos' : None }
		self.dados['Valor Total do II'] = { 'total_ii' : None }
		self.dados['Valor do PIS'] = { 'pis' : None }
		self.dados['Valor da COFINS'] = { 'cofins' : None }
		self.dados['Valor Aproximado dos Tributos'] = { 'valor_aproximado_tributos' : None }


	def add(self, label, dados):
		label = label.replace("\n", '')
		label = label.strip()

		if label in self.dados:
			for i in self.dados[label]:
				dados = dados.replace("\n", '')
				dados = dados.strip()
				if dados not in '': ### necessário adicionar essa regra para evitar muitas colunas com valor '' ao invés de null
					self.dados[label][i] = dados

	def atualizarLista(self, lista, label):
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]

	def get(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista

	def __str__(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista.__str__()