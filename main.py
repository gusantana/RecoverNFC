from time import *
from socket import *
from http.client import HTTPConnection
import threading

import sqlite3 as database
import select

url_completa = 'http://www.sefaz.mt.gov.br/nfce/consultanfce?chNFe=51171047508411155940650690001703751000144339&nVersao=100&tpAmb=1&dhEmi=323031372d31302d30325431383a32313a34382d30343a3030&vNF=99.90&vICMS=0.00&digVal=726c564737336a667576387665673339676d77705547772b3569673d&cIdToken=000001&cHashQRCode=98BD5C7C79F7B01E5EF5A6365E741D4B1C7718AA'

def main ():
    connection = HTTPConnection ('www.sefaz.mt.gov.br', 80)
    connection.set_debuglevel(2)
    header = {}
    header['Connection'] = 'keep-alive'
    header['Cache-Control'] = 'max-age=0'
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    header['Upgrade-Insecure-Requests'] = '1'
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    header['Accept-Encoding'] = 'gzip, deflate, br'
    header['Accept-Language'] = 'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4'
    
    query = 'nfce/consultanfce?chNFe=51171047508411155940650690001703751000144339&nVersao=100&tpAmb=1&dhEmi=323031372d31302d30325431383a32313a34382d30343a3030&vNF=99.90&vICMS=0.00&digVal=726c564737336a667576387665673339676d77705547772b3569673d&cIdToken=000001&cHashQRCode=98BD5C7C79F7B01E5EF5A6365E741D4B1C7718AA'
    connection.request('GET', query, None, header)
    resposta = connection.getresponse()
    print(resposta.read())
    
    print('conectou')

main ()