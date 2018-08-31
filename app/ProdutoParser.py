from core.BaseParser import BaseParser
import re

class ProdutoParser (BaseParser):
	def __init__(self):
		BaseParser.__init__(self)
		self.tags_validos = ('td', 'table')
		self.tag_itens = 'A + '
		self.tags_tit_produto = ('class', 'fixo-prod-serv-descricao')
		self.tags_qtd_produto = ('class', 'fixo-prod-serv-qtd')
		self.tags_unidade_comercial = ('class', 'fixo-prod-serv-uc')
		self.tags_valor_produto = ('class', 'fixo-prod-serv-vb')

		self.gravar_descricao = False
		self.gravar_qtd_produto = False
		self.gravar_unidade_comercial = False
		self.gravar_valor_produto = False

		self.gravar_label = False
		self.gravar_dados = False

		self.cur_item = 0
		self.dados = {}
		self.dados['itens'] = {}

		self.gravando_info_adicional = False

	def mudar_tags_validas(self, contexto):
		if 'adicionais_produto' in contexto:
			self.tags_validos = ('span', 'label')
			self.gravando_info_adicional = True
		if 'geral' in contexto:
			self.tags_validos = ('td', 'table')
			self.gravando_info_adicional = False


	
	def handle_starttag(self, tag, atributos):
		if tag not in self.tags_validos:
			return

		if 'label' in tag and self.gravando_info_adicional:
			self.gravar_label = True

		if 'span' in tag and self.gravando_info_adicional:
			self.gravar_dados = True

		for nome, valor in atributos:
			if 'table' in tag and 'id' in nome and self.tag_itens in valor:
				self.cur_item = int(valor[valor.find(self.tag_itens) + len(self.tag_itens):])
				self.dados['itens'][self.cur_item] = {}
				
			if 'table' in tag and 'id' in nome and str(self.cur_item) == valor:
				self.dados['itens'][self.cur_item]['info_adicional'] = {}
				self.mudar_tags_validas('adicionais_produto')
				
			if nome in self.tags_tit_produto and valor in self.tags_tit_produto:
				self.gravar_descricao = True
			if nome in self.tags_qtd_produto and valor in self.tags_qtd_produto:
				self.gravar_qtd_produto = True
			if nome in self.tags_unidade_comercial and valor in self.tags_unidade_comercial:
				self.gravar_unidade_comercial = True
			if nome in self.tags_valor_produto and valor in self.tags_valor_produto:
				self.gravar_valor_produto = True


	def handle_endtag(self, tag):
		if 'table' in tag and self.gravando_info_adicional:
			self.mudar_tags_validas('geral')


	def handle_data(self, data):
		if self.gravar_descricao: 
			#self.dados['itens'][self.cur_item]['']
			#print(data)
			self.gravar_descricao = False

		if self.gravar_qtd_produto:
			#print(data)
			self.gravar_qtd_produto = False

		if self.gravar_unidade_comercial:
			#print(data)
			self.gravar_unidade_comercial = False

		if self.gravar_valor_produto:
			#print(data)
			self.gravar_valor_produto = False

		if self.gravar_label and self.gravando_info_adicional:
			print('Label: {}'.format(data))
			self.gravar_label = False

		if self.gravar_dados and self.gravando_info_adicional:
			print('Dado: {}'.format(data))
			self.gravar_dados = False