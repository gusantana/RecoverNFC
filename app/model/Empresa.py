import re

class Empresa:
	def __init__(self):
		self.dados = {}
		self.dados['Nome / Razão Social'] = { 'razao_social' : None }
		self.dados['Nome Fantasia'] = { 'nome_fantasia' : None }
		self.dados['CNPJ'] = { 'cnpj' : None }
		self.dados['Endereço'] = { 'endereco' : None }
		self.dados['Numero'] = { 'numero': None}
		self.dados['Bairro / Distrito'] = { 'bairro' : None }
		self.dados['CEP'] = { 'cep' : None }
		self.dados['Município'] = { 'municipio' : None }
		self.dados['Telefone'] = { 'telefone' : None }
		self.dados['UF'] = { 'uf' : None }
		self.dados['País'] = { 'pais' : None }
		self.dados['Inscrição Estadual'] = { 'inscricao_estadual' : None }
		self.dados['Inscrição Estadual do Substituto Tributário'] = { 'ie_substituto_tributario' : None }
		self.dados['Inscrição Municipal'] = { 'inscricao_municipal' : None }
		self.dados['Município da Ocorrência do Fato Gerador do ICMS'] = { 'municipio_gerador_icms' : None }
		self.dados['CNAE Fiscal'] = { 'cnae_fiscal' : None }
		self.dados['Código de Regime Tributário'] = { 'cod_regime_tributario' : None }


	def add(self, label, dados):
		label = label.replace("\n", '')
		label = label.strip()

		if label in self.dados:
			for i in self.dados[label]:
				if 'Endereço' in label and ',' in dados:
					via, numero = dados.split(',')
					numero = numero.replace('\n', '')
					numero = numero.replace('\xa0', '')
					numero = numero.strip()
					self.dados['Endereço']['endereco'] = via
					self.dados['Numero']['numero'] = numero
					return
				dados = dados.replace('\n', '')
				dados = dados.replace('\xa0', '')
				dados = dados.strip()
				dados = re.sub('^[0-9]+\s+-\s+', '', dados)

				self.dados[label][i] = dados


	def __str__(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista.__str__()


	def get(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista