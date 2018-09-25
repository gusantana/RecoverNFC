import re

class NFCe:
	
	def __init__(self):
		self.dados = {}
		self.dados['Modelo'] = {'modelo': 0}
		self.dados['Série'] = {'serie' : 0}
		self.dados['Número'] = {'numero' : 0}
		self.dados['Data de Emissão'] = {'data_emissao' : None}
		self.dados['Data Saída/Entrada'] = {'data_saida_entrada' : None}
		self.dados['Valor Total da Nota Fiscal'] = {'total_nota' : 0.0}
		self.cnpj = None
		self.razao_social = None
		self.ie = None
		self.uf = None
		self.dados['Versão do Processo'] = {'versao_processo' : None}
		self.dados['Tipo de Emissão'] = {'tipo_emissao' : None}
		self.dados['Finalidade'] = {'finalidade' : None}
		self.dados['Natureza da Operação'] = {'natureza_operacao' : None}
		self.dados['Tipo da Operação'] = {'tipo_operacao' : None}
		self.dados['Forma de Pagamento'] = {'forma_pagamento' : None}
		self.digest_value = None
		self.dados['Eventos da NFC-e'] = {'eventos_nfce' : None}
		self.dados['Protocolo'] = {'protocolo' : None}
		self.dados['Data Autorização'] = {'data_autorizacao' : None}
		self.dados['Data Inclusão BD'] = {'data_inclusao_bd' : None}
		self.autorizacao_uso = None

	def add(self, label, dados):
		label = label.replace("\n", '')
		label = label.strip()

		if label in self.dados:
			for i in self.dados[label]:
				dados = dados.replace("\n", '')
				dados = dados.strip()
				dados = re.sub('^[0-9] - ', '', dados)
				self.dados[label][i] = dados

	
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

