from django.shortcuts import render
from django.http import HttpResponse

from .models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all()

    html = ""
    html += "<h1>Lista de Pessoas</h1>"
    html += "<table border='1' cellpadding='8' cellspacing='0'>"
    html += "<thead><tr><th>ID</th><th>Nome</th><th>Ações</th></tr></thead>"
    html += "<tbody>"

    for pessoa in pessoas:
        html += f"<tr>"
        html += f"<td>{pessoa.id}</td>"
        html += f"<td>{pessoa.nome}</td>"
        html += f"<td>"
        html += f"<a href='/pessoa/{pessoa.id}/'>Detalhar</a> | "
        html += f"<a href='/pessoa/edit/{pessoa.id}/'>Editar</a> | "
        html += f"<a href='/pessoa/delete/{pessoa.id}/'>Deletar</a>"
        html += f"</td>"
        html += f"</tr>"

    html += "</tbody>"
    html += "</table>"

    return HttpResponse(html)


def detail(request, id):
    return HttpResponse("Detalhando a pessoa de id " + str(id) + "!")

def add(request):
    return HttpResponse("Adicionando pessoa.")

def edit(request, id):
    return HttpResponse("Editando a pessoa de id " + str(id) + "!")

def delete(request, id):
    return HttpResponse("Apagando a pessoa de id " + str(id) + "!")

def toList(request):
    pessoas = Pessoa.objects.all()

    html = ""
    html += "<h1>Lista de Pessoas</h1>"
    html += "<table border='1' cellpadding='8' cellspacing='0'>"
    html += "<thead><tr><th>ID</th><th>Nome</th><th>Ações</th></tr></thead>"
    html += "<tbody>"

    for pessoa in pessoas:
        html += f"<tr>"
        html += f"<td>{pessoa.id}</td>"
        html += f"<td>{pessoa.nome}</td>"
        html += f"<td>"
        html += f"<a href='/pessoa/{pessoa.id}/'>Detalhar</a> | "
        html += f"<a href='/pessoa/edit/{pessoa.id}/'>Editar</a> | "
        html += f"<a href='/pessoa/delete/{pessoa.id}/'>Deletar</a>"
        html += f"</td>"
        html += f"</tr>"

    html += "</tbody>"
    html += "</table>"

    return HttpResponse(html)