from core.BaseParser import BaseParser
import re

class NFCParser (BaseParser):
	def __init__(self):
		BaseParser.__init__(self)
		self.valorTotal = 0
		self.dados = {}
		self.dados['itens'] = {}
		self.dados['empresa'] = {}

		self.cur_item = 0
		self.cur_desc_item = ''
		self.gravar_dados_itens = False
		self.gravar_nome_produto = False
		self.gravar_valor_produto = False
		self.gravar_cod_produto = False
		self.gravar_qtd_produto = False
		self.passo_1_qtd_produto = False
		self.gravar_data_emissao = False
		self.passo_1_data_emissao = False
		self.gravar_chave_nota  = False
		self.gravar_razao_social = False
		self.gravar_cnpj        = False
		self.gravar_endereco    = False

	def handle_starttag(self, tag, atributos):
		if tag not in self.tags_validos:
			return
		for nome, valor in atributos:
			if 'id' in nome and self.tag_itens in valor:
				self.cur_item = int(valor[valor.find(self.tag_itens) + len(self.tag_itens):])
				self.gravar_dados_itens = True
			if nome in self.tags_tit_produto and valor in self.tags_tit_produto:
				self.gravar_nome_produto = True
				self.dados['itens'][self.cur_item] = {}
			if nome in self.tags_valor_produto and valor in self.tags_valor_produto:
				self.gravar_valor_produto = True
			if nome in self.tags_cod_produto and valor in self.tags_cod_produto:
				self.gravar_cod_produto = True
			if nome in self.tags_qtd_produto and valor in self.tags_qtd_produto:
				self.gravar_qtd_produto = True
			if nome in self.tags_chave and valor in self.tags_chave:
				self.gravar_chave_nota = True
			if nome in self.tags_data_emissao and valor in self.tags_data_emissao:
				self.gravar_data_emissao = True
				self.adicionarTag()
			if nome in self.tags_razao_social and valor in self.tags_razao_social:
				self.gravar_razao_social = True
				self.adicionarTag()
			if nome in self.tags_endereco and valor in self.tags_endereco:
				self.gravar_endereco = True
			if nome in self.tags_cnpj and valor in self.tags_cnpj:
				self.gravar_cnpj = True




	def handle_endtag(self, tag):
		if self.valorTotal == 1:
			if (tag == 'span'):
				self.valorTotal = 0
		if (tag == 'table'):
			self.acabouTabela = 1




	def handle_data(self, data):
		if self.valorTotal == 1:
			self.dados['valorTotal'] = data
			self.valorTotal = 0
		if self.gravar_razao_social:
			if data not in ('\n', '\r\n, \r'):
				self.dados['empresa']['razao_social'] = data
			self.gravar_razao_social = False
		if self.gravar_cnpj:
			if 'CNPJ' in data:
				self.dados['empresa']['cnpj'] = data.split(':')[1].strip(' \n\t')

		if self.gravar_endereco:
			if data not in ('\n', '\t', '\r') and 'CNPJ' not in data:
				endereco = data.replace('\n', '').replace('\t', '').split(',')
				self.dados['empresa']['via'] = endereco[0].strip()
				self.dados['empresa']['numero'] = endereco[1].strip()
				self.dados['empresa']['bairro'] = endereco[3].strip()
				self.dados['empresa']['cidade'] = endereco[4].strip()
				self.dados['empresa']['estado'] = endereco[5].strip()
				#print (via, numero, nulo, bairro, cidade, estado)
				#self.dados['empresa']['endereco'] = 
				self.gravar_endereco = False


		if self.gravar_dados_itens:
			if self.gravar_nome_produto:
				self.dados['itens'][self.cur_item]['descricao'] = data
				self.gravar_nome_produto = False
			if self.gravar_valor_produto:
				self.dados['itens'][self.cur_item]['valor'] = data
				self.gravar_valor_produto = False
			if self.gravar_cod_produto:
				d = re.search('(?<=[ ])[0-9]*', data)
				if (d):
					d = d.group(0) #pega o resultado
					self.dados['itens'][self.cur_item]['codigo'] = d
				self.gravar_cod_produto = False
			if self.gravar_qtd_produto:
				if (self.passo_1_qtd_produto):
					self.dados['itens'][self.cur_item]['quantidade'] = data
					self.gravar_qtd_produto = False
					self.passo_1_qtd_produto = False
					return
				self.passo_1_qtd_produto = True
			if self.gravar_data_emissao:
				if self.passo_1_data_emissao:
					if '[##' in data:
						d = re.search('[0-9]*-[0-1][0-9]-[0-9]*[ ]+[0-2][0-9]:[0-6][0-9]:[0-6][0-9]', data)
						if (d):
							d = d.group(0)
							self.dados['data_hora'] = d
						self.gravar_data_emissao = False
				self.passo_1_data_emissao = True
			if self.gravar_chave_nota:
				self.dados['chave'] = data.replace(" ", "")
				self.dados['chave_str'] = data
				self.gravar_chave_nota = False




	def __len__(self):
		return len(self.dados)

	def get(self):
		return self.dados
