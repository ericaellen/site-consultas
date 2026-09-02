from django.shortcuts import render
from django.http import HttpResponse

from .models import Consulta

def index(request):
    consultas = Consulta.objects.all()

    html = ""
    html += "<h1>Lista de Consultas</h1>"
    html += "<table border='1' cellpadding='8' cellspacing='0'>"
    html += "<thead><tr><th>ID</th><th>Data e Hora</th><th>Ações</th></tr></thead>"
    html += "<tbody>"

    for consulta in consultas:
        html += f"<tr>"
        html += f"<td>{consulta.id}</td>"
        html += f"<td>{consulta.dataHora}</td>"
        html += f"<td>"
        html += f"<a href='/consulta/{consulta.id}/'>Detalhar</a> | "
        html += f"<a href='/consulta/edit/{consulta.id}/'>Editar</a> | "
        html += f"<a href='/consulta/delete/{consulta.id}/'>Deletar</a>"
        html += f"</td>"
        html += f"</tr>"

    html += "</tbody>"
    html += "</table>"

    return HttpResponse(html)

def detail(request, id):
    return HttpResponse("Detalhando a consulta de id " + str(id) + "!")

def add(request):
    return HttpResponse("Adicionando consulta.")

def edit(request, id):
    return HttpResponse("Editando consulta de id " + str(id) + "!")

def delete(request, id):
    return HttpResponse("Apagando consulta de id " + str(id) + "!")

def toList(request):
    consultas = Consulta.objects.all()

    html = ""
    html += "<h1>Lista de Consultas</h1>"
    html += "<table border='1' cellpadding='8' cellspacing='0'>"
    html += "<thead><tr><th>ID</th><th>Data e Hora</th><th>Ações</th></tr></thead>"
    html += "<tbody>"

    for consulta in consultas:
        html += f"<tr>"
        html += f"<td>{consulta.id}</td>"
        html += f"<td>{consulta.dataHora}</td>"
        html += f"<td>"
        html += f"<a href='/consulta/{consulta.id}/'>Detalhar</a> | "
        html += f"<a href='/consulta/edit/{consulta.id}/'>Editar</a> | "
        html += f"<a href='/consulta/delete/{consulta.id}/'>Deletar</a>"
        html += f"</td>"
        html += f"</tr>"

    html += "</tbody>"
    html += "</table>"

    return HttpResponse(html)
