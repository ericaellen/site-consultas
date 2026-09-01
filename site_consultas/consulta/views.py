from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Configurações de consulta")

def add(request):
    return HttpResponse("Adicionando consulta.")

def editar(request):
    return HttpResponse("Editando consulta.")

def apagar(request):
    return HttpResponse("Apagando consulta.")

def listar(request):
    return HttpResponse("Listando consultas.")
