from html import parser
import re

class BaseParser(parser.HTMLParser):
    def __init__(self):
        parser.HTMLParser.__init__(self)
        self.tags_validos       = ('span', 'tr')
        self.tags_tit_produto   = ('class', 'txtTit')
        self.tag_itens          = 'Item + '
