#Parser correspondente da aba NFCe
from pprint import *
from html import parser
import re

class EmitenteParser(parser.HTMLParser):
	def __init__(self):
		parser.HTMLParser.__init__(self)
		self.tags_tabela = ('td')

	def handle_starttag(self, tag, atributos):
		if tag in self.tags_tabela:
			print('<{}>'.format(tag))
		

	def handle_endtag(self,tag):
		if tag in self.tags_tabela:
			print("</{}>".format(tag))

	def handle_data(self, data):
		print (data.strip())