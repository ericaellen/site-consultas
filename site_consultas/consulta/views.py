from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from .forms import ConsultaForm
from .models import Consulta


def index(request):
    # Busca todas as consultas para mostrar na lista.
    consultas = Consulta.objects.all()
    return render(request, 'consulta/lista.html', {'consultas': consultas})


def detail(request, id):
    # Busca a consulta pelo ID; se não existir, responde com página não encontrada.
    try:
        consulta = Consulta.objects.get(id=id)
    except Consulta.DoesNotExist:
        return HttpResponseNotFound('Consulta não encontrada.')

    return render(request, 'consulta/detalhar.html', {'consulta': consulta})


def add(request):
    # No envio, valida os dados antes de salvar a consulta.
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/consulta/')
    else:
        # Ao abrir a página, mostra um formulário vazio.
        form = ConsultaForm()

    return render(request, 'consulta/adicionar.html', {
        'form': form,
        'titulo': 'Adicionar consulta'
    })


def edit(request, id):
    # Busca a consulta que será editada.
    try:
        consulta = Consulta.objects.get(id=id)
    except Consulta.DoesNotExist:
        return HttpResponseNotFound('Consulta não encontrada.')

    if request.method == 'POST':
        # Usa a consulta existente para atualizar, em vez de criar outra.
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/consulta/')
    else:
        # Preenche o formulário com os dados atuais da consulta.
        form = ConsultaForm(instance=consulta)

    return render(request, 'consulta/editar.html', {
        'form': form,
        'titulo': 'Editar consulta'
    })


def delete(request, id):
    # Busca a consulta que será mostrada na confirmação.
    try:
        consulta = Consulta.objects.get(id=id)
    except Consulta.DoesNotExist:
        return HttpResponseNotFound('Consulta não encontrada.')

    if request.method == 'POST':
        consulta.delete()
        return redirect('/consulta/')

    # No GET, só mostra a confirmação; ainda não exclui.
    return render(request, 'consulta/deletar.html', {'consulta': consulta})


def toList(request):
    # Mantém a rota /list/ exibindo a mesma lista de consultas.
    consultas = Consulta.objects.all()
    return render(request, 'consulta/lista.html', {'consultas': consultas})
