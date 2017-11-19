from html import parser
import re

class BaseParser(parser.HTMLParser):
    def __init__(self):
        parser.HTMLParser.__init__(self)
        self.tags_validos       = ('span', 'tr')
        self.tags_tit_produto   = ('class', 'txtTit')
        self.tags_valor_produto = ('class', 'valor')
        self.tags_cod_produto   = ('class', 'RCod')
        self.tags_qtd_produto   = ('class', 'Rqtd')
        self._tag_qtd_produto   = ('strong')
        self.tag_itens          = 'Item + '

        self.tag_forma_pagamento = '<label>Forma de pagamento:</label><span class="totalNumb txtTitR">Valor pago R$:</span></div><div id="linhaTotal"><label class="tx">'
