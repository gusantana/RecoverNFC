import requests
from base64 import *
import sys

string_base_64 = b64encode(b'https://www.sefaz.mt.gov.br/nfce/consultanfce?chNFe=51171047508411155940650690001703751000144339&nVersao=100&tpAmb=1&dhEmi=323031372d31302d30325431383a32313a34382d30343a3030&vNF=99.90&vICMS=0.00&digVal=726c564737336a667576387665673339676d77705547772b3569673d&cIdToken=000001&cHashQRCode=98BD5C7C79F7B01E5EF5A6365E741D4B1C7718AA')
url = 'http://127.0.0.1:8000/send/{}'.format(string_base_64.decode('ascii'))

r = requests.get(url)

print(r.text)