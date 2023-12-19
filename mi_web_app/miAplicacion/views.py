from django.shortcuts import render

from django.http import HttpResponse

def index(http):
	return HttpResponse('''<h1> Mi primera aplicación </h1><h2> Has llegado a index creado.''')
 