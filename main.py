from time import *
from socket import *
from http.client import HTTPConnection
import threading
import requests
import sqlite3 as database
import select
from app.NFCParser import NFCParser
from app.business.NotaBO import NotaBO

url_completa = 'https://www.sefaz.mt.gov.br/nfce/consultanfce?chNFe=51171047508411155940650690001703751000144339&nVersao=100&tpAmb=1&dhEmi=323031372d31302d30325431383a32313a34382d30343a3030&vNF=99.90&vICMS=0.00&digVal=726c564737336a667576387665673339676d77705547772b3569673d&cIdToken=000001&cHashQRCode=98BD5C7C79F7B01E5EF5A6365E741D4B1C7718AA'

url_dois_itens = 'https://www.sefaz.mt.gov.br/nfce/consultanfce?chNFe=51171109477652003454651080001764329093430088&nVersao=100&tpAmb=1&dhEmi=323031372d31312d30335431343a33303a30382d30343a3030&vNF=7.92&vICMS=0.00&digVal=647562535a7a43767a726c67556e33357643626d4f2f47676739303d&cIdToken=000001&cHashQRCode=669483A3BF8617A7877E80E8A976C9A2F8275C84'

url_varios_itens = 'https://www.sefaz.mt.gov.br/nfce/consultanfce?chNFe=51171109477652003454651030002291979093707297&nVersao=100&tpAmb=1&dhEmi=323031372d31312d30355431383a30373a32392d30343a3030&vNF=27.73&vICMS=0.00&digVal=4c564f666d317a38746e416d6c7155574a4a38636b523432594a4d3d&cIdToken=000001&cHashQRCode=754D122011BEA8C1050659866AA09BBCB03CD271'

url_teste = 'https://www.sefaz.mt.gov.br/nfce/consultanfce?chNFe=51180109477652000943651040000195201090942311&nVersao=100&tpAmb=1&dhEmi=323031382d30312d33315431393a34323a33312d30333a3030&vNF=40.60&vICMS=0.00&digVal=79326a2f716f654854686c4d3445774a337959336f50706d4374303d&cIdToken=000001&cHashQRCode=15ADC327DBAA8871AAB213228C59D32CCC6C2A4F'

def main ():
    conexao = database.connect('db.db')
    file = open('parsed.txt', 'r')
    notaBo = NotaBO (conexao)

    try:
        for linha in file:
            parser = NFCParser()
            if linha.startswith('http://', 0, len('http://')):
                linha = linha.replace('http://', 'https://')
            linha = linha.strip(' \n')
            r = requests.get(linha)
            #print (r.text)
            parser.feed(r.text)
            parser.dados['url'] = linha
            notaBo.write(parser.dados)
            #print(parser.dados)
    except Exception as e:
        print (e)
    
        

    

main ()
