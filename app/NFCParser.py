from core.BaseParser import BaseParser
import re

class NFCParser (BaseParser):
    def __init__(self):
        BaseParser.__init__(self)
        self.valorTotal = 0
        self.dados = {}

        self.cur_item = 0
        self.cur_desc_item = ''
        self.gravar_dados_itens = False
        self.gravar_nome_produto = False
        self.gravar_valor_produto = False
        self.gravar_cod_produto = False
        self.gravar_qtd_produto = False

    def handle_starttag(self, tag, atributos):
        if (tag not in self.tags_validos):
            return
        for nome, valor in atributos:
            # if 'txtMax' in valor:
            #     self.valorTotal = 1
            if 'id' in nome and self.tag_itens in valor:
                self.cur_item = valor[valor.find(self.tag_itens) + len(self.tag_itens):]
                self.gravar_dados_itens = True
            if nome in self.tags_tit_produto and valor in self.tags_tit_produto:
                self.gravar_nome_produto = True
                self.dados[self.cur_item] = {}
            if nome in self.tags_valor_produto and valor in self.tags_valor_produto:
                self.gravar_valor_produto = True
            if nome in self.tags_cod_produto and valor in self.tags_cod_produto:
                self.gravar_cod_produto = True
            if nome in self.tags_qtd_produto and valor in self.tags_qtd_produto:
                self.gravar_qtd_produto = True


        
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
        if self.gravar_dados_itens:
            if self.gravar_nome_produto:
                self.dados[self.cur_item]['descricao'] = data
                self.gravar_nome_produto = False
            if self.gravar_valor_produto:
                self.dados[self.cur_item]['valor'] = data
                self.gravar_valor_produto = False
            if self.gravar_cod_produto:
                self.dados[self.cur_item]['codigo'] = data
                self.gravar_cod_produto = False
            if self.gravar_qtd_produto:
                self.dados[self.cur_item]['quantidade'] = data
                self.gravar_qtd_produto = False

