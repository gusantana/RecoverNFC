from html import parser

class NFCParser (parser.HTMLParser): 
    def __init__(self):
        parser.HTMLParser.__init__(self)
        self.gravar = 0
        self.dados = []

    def handle_starttag(self, tag, atributos):
        if (tag != 'span'):
            return
        for nome, valor in atributos:
            if 'txtMax' in valor:
                self.gravar = 1
                print (valor)
            
        
    def handle_endtag(self, tag):
        if self.gravar == 1:
            if (tag == 'span'):
                self.gravar = 0

    def handle_data(self, data):
        if self.gravar == 1:
            self.dados.append(data)

