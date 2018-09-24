import re

class InfoAdicional:
	def __init__(self, conexao = None):
		self.conexao = conexao
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


	def write(self):
		try:
			cur = self.conexao.cursor()
			info_adicional = dados['info_adicional']
			id_nota = dados['nfce']['id']

			sql = '''INSERT INTO info_adicional (id_nota, descricao, imposto_estadual, imposto_federal, qr_code) VALUES (?, ?, ?, ?, ?)'''

			param = (id_nota, info_adicional['descricao'], info_adicional['imposto_estadual'], info_adicional['imposto_federal'], info_adicional['qr_code'])

			cur.execute(sql, param)
			
		except Exception as e:
			raise e