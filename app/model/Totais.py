import re

class Totais:
	def __init__(self, conexao = None):
		self.conexao = conexao
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
		self.dados['Valor do PIS'] = { 'pis' : 0.0 }
		self.dados['Valor da COFINS'] = { 'cofins' : None }
		self.dados['Valor Aproximado dos Tributos'] = { 'valor_aproximado_tributos' : 0.0 }


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


	def write(self, dados):
		try:
			totais = dados['totais']
			id_nota = dados['nfce']['id']

			cur = self.conexao.cursor()

			sql = '''INSERT INTO totais (
						id_nota,
						base_icms,
						base_icms_st,
						pis,
						cofins,
						frete,
						icms_desonerado,
						icms_substituicao,
						outras_despesas_acessorias,
						seguro,
						total_descontos,
						total_ii,
						total_nfe,
						valor_icms,
						valor_total_produtos,
						valor_aproximado_tributos)
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

			param = (id_nota, totais['base_icms'], totais['base_icms_st'], totais['pis'], totais['cofins'], totais['frete'], totais['icms_desonerado'], totais['icms_substituicao'], totais['outras_despesas_acessorias'], totais['seguro'], totais['total_descontos'], totais['total_ii'],
				totais['total_nfe'], totais['valor_icms'], totais['valor_total_produtos'], totais['valor_aproximado_tributos'])

			cur.execute(sql, param)
		except Exception as e:
			raise e