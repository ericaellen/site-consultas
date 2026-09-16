from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/lista.html', {'pessoas': pessoas})


def detail(request, id):
    return render(request, 'pessoa/detalhar.html', {'id': id})

def add(request):
    return HttpResponse("Adicionando pessoa.")

def edit(request, id):
    return render(request, 'pessoa/editar.html', {'id': id})

def delete(request, id):
    return render(request, 'pessoa/deletar.html', {'id': id})

def toList(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/lista.html', {'pessoas': pessoas})
