import re

class Empresa:
	def __init__(self):
		self.dados = {}
		self.dados['Nome / Razão Social'] = { 'razao_social' : '' }
		self.dados['Nome Fantasia'] = { 'nome_fantasia' : '' }
		self.dados['CNPJ'] = { 'cnpj' : '' }
		self.dados['Endereço'] = { 'endereco' : '' }
		self.dados['Numero'] = { 'numero': ''}
		self.dados['Bairro / Distrito'] = { 'bairro' : '' }
		self.dados['CEP'] = { 'cep' : '' }
		self.dados['Município'] = { 'municipio' : '' }
		self.dados['Telefone'] = { 'telefone' : '' }
		self.dados['UF'] = { 'uf' : '' }
		self.dados['País'] = { 'pais' : '' }
		self.dados['Inscrição Estadual'] = { 'inscricao_estadual' : '' }
		self.dados['Inscrição Estadual do Substituto Tributário'] = { 'ie_substituto_tributario' : '' }
		self.dados['Inscrição Municipal'] = { 'inscricao_municipal' : '' }
		self.dados['Município da Ocorrência do Fato Gerador do ICMS'] = { 'municipio_gerador_icms' : '' }
		self.dados['CNAE Fiscal'] = { 'cnae_fiscal' : '' }
		self.dados['Código de Regime Tributário'] = { 'cod_regime_tributario' : '' }


	def add(self, label, dados):
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
				dados = re.sub('^[0-9]*\s+-\s+', '', dados)

				self.dados[label][i] = dados


	def __str__(self):
			lista = {}
			for label in self.dados:
				for i in self.dados[label]:
					lista[i] = self.dados[label][i]
			return lista.__str__()


