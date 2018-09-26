from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Está")

def send(request):
	return 