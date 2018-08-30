import re

class NFCe:
	
	def __init__(self):
		self.dados = {}
		self.dados['Modelo'] = {'modelo': 0}
		self.dados['Série'] = {'serie' : 0}
		self.dados['Número'] = {'numero' : 0}
		self.dados['Data de Emissão'] = {'data_emissao' : ""}
		self.dados['Data Saída/Entrada'] = {'data_saida_entrada' : ""}
		self.dados['Valor Total da Nota Fiscal'] = {'total_nota' : 0.0}
		self.cnpj = ""
		self.razao_social = ""
		self.ie = ""
		self.uf = ""
		self.dados['Versão do Processo'] = {'versao_processo' : ""}
		self.dados['Tipo de Emissão'] = {'tipo_emissao' : ""}
		self.dados['Finalidade'] = {'finalidade' : ""}
		self.dados['Natureza da Operação'] = {'natureza_operacao' : ""}
		self.dados['Tipo da Operação'] = {'tipo_operacao' : ""}
		self.dados['Forma de Pagamento'] = {'forma_pagamento' : ""}
		self.digest_value = ""
		self.dados['Eventos da NFC-e'] = {'eventos_nfce' : ""}
		self.dados['Protocolo'] = {'protocolo' : ""}
		self.dados['Data Autorização'] = {'data_autorizacao' : ""}
		self.dados['Data Inclusão BD'] = {'data_inclusao_bd' : ""}
		self.autorizacao_uso = ""

	def add(self, label, dados):
		if label in self.dados:
			for i in self.dados[label]:
				dados = dados.replace("\n", '')
				dados = dados.strip()
				dados = re.sub('^[0-9] - ', '', dados)
				self.dados[label][i] = dados

	def __str__(self):
		lista = {}
		for label in self.dados:
			for i in self.dados[label]:
				lista[i] = self.dados[label][i]
		return lista.__str__()

