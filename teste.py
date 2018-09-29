import requests
from base64 import *
import sys

string_base_64 = b64encode(b'url_de_testeasdasdasdasdsadasdasd')
url = 'http://127.0.0.1:8000/send/{}'.format(string_base_64.decode('ascii'))

r = requests.get(url)

print(r.text)