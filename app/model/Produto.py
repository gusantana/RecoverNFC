import re

class Produto:
	def __init__(self, conexao = None):
		self.conexao = conexao
		self.dados = {}
		self.dados['Código do Produto'] = { 'codigo' : None }
		self.dados['Código NCM'] = { 'codigo_ncm' : None }
		self.dados['Código CEST'] = { 'codigo_cest' : None }
		self.dados['Código EX da TIPI'] = { 'codigo_ex_tipi' : None }
		self.dados['CFOP'] = { 'cfop' : None }
		self.dados['Outras Despesas Acessórias'] = { 'outras_despesas_acessorias' : None}
		self.dados['Valor do Desconto'] = { 'valor_desconto' : None }
		self.dados['Valor Total do Frete'] = { 'valor_frete' : None }
		self.dados['Valor do Seguro'] = { 'valor_seguro' : None }

		self.dados['Código EAN Comercial'] = { 'cod_ean_comercial' : None }
		self.dados['Origem da Mercadoria'] = { 'origem_mercadoria' : None }
		self.dados['Tributação do ICMS'] = { 'tributacao_icms' : None }

		#pis
		#self.dados['CST'] = { 'pis_cst' : '' }




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


	def write(self, dados):
		try:
			cur = self.conexao.cursor
			dados_produtos = dados['produtos']
			id_nota = dados['nfce']['id']

			sql = '''INSERT INTO item (id_nota, descricao, codigo, quantidade, unidade_comercial, valor) VALUES (?, ?, ?, ?, ?, ?)'''

			for index in dados_produtos:
				produto = dados_produtos[index]
				param = (id_nota, produto['descricao'], produto['info_adicional']['codigo'], produto['qtd'], )
		except Exception as e:
			raise e