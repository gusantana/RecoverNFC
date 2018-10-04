from django.shortcuts import render
from django.http import HttpResponse
from base64 import *
import sys
import nfce

def index(request):
    return HttpResponse('asd')


def send(request, url):
	url = b64decode(url.replace('_', '/'))
	parser = nfce.Nfc()
	resposta = parser.write(url)
	return HttpResponse('{}'.format(resposta))