from django.shortcuts import render
from django.http import HttpResponse
from base64 import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def send(request, url):
	url = b64decode(url)
	return HttpResponse(url)