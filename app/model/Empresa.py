import re

class Empresa:
	def __init__(self, conexao = None):
		self.conexao = conexao
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


	def write(self, dados):
		try:
			cur = self.conexao.cursor()
			dados_empresa = dados['empresa']

			try:
				sql = '''SELECT id FROM empresa where cnpj = ?'''
				param = (dados_empresa['cnpj'],)
				cur.execute(sql, param)
				id_empresa = cur.fetchone()[0]
				
			except Exception as e:
				sql = '''INSERT INTO empresa (razao_social, cnpj, nome_fantasia, inscricao_estadual, endereco, numero, bairro, municipio, uf, cep, telefone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
				
				param = (dados_empresa['razao_social'], dados_empresa['cnpj'], dados_empresa['nome_fantasia'], dados_empresa['inscricao_estadual'], dados_empresa['endereco'], dados_empresa['numero'], dados_empresa['bairro'], dados_empresa['municipio'], dados_empresa['uf'], dados_empresa['cep'], dados_empresa['telefone'])

				cur.execute(sql, param)

				cur = self.conexao.cursor()
				cur.execute("SELECT last_insert_rowid()")
				id_empresa = cur.fetchone()[0]

			finally:
				dados['empresa']['id'] = id_empresa
		except Exception as e:
			raise e
