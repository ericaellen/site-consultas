from django.shortcuts import render
from django.http import HttpResponse
from .models import Consulta

def index(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/lista.html', {'consultas': consultas})

def detail(request, id):
    return render(request, 'consulta/detalhar.html', {'id': id})

def add(request):
    return render(request, 'consulta/adicionar.html')

def edit(request, id):
    return render(request, 'consulta/editar.html', {'id': id})

def delete(request, id):
    return render(request, 'consulta/deletar.html', {'id': id})

def toList(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/lista.html', {'consultas': consultas})
