from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo!")

def add(request):
    return HttpResponse("Adicionando pessoa.")

def editar(request):
    return HttpResponse("Editando pessoa.")

def apagar(request):
    return HttpResponse("Apagando pessoa.")

def listar(request):
    return HttpResponse("Listando pessoas.")