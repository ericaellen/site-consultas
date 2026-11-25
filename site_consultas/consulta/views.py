from django.shortcuts import get_object_or_404, redirect, render
from .forms import ConsultaForm
from .models import Consulta


def lista_consultas(request):
    # Busca todas as consultas para mostrar na lista.
    consultas = Consulta.objects.all()
    return render(request, 'consulta/lista.html', {'consultas': consultas})


def detalhar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    return render(request, 'consulta/detalhar.html', {'consulta': consulta})


def adicionar_consulta(request):
    # No envio, valida os dados antes de salvar a consulta.
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta:lista_consultas')
    else:
        # Ao abrir a página, mostra um formulário vazio.
        form = ConsultaForm()

    return render(request, 'consulta/adicionar.html', {
        'form': form,
        'titulo': 'Adicionar consulta'
    })


def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        # Usa a consulta existente para atualizar, em vez de criar outra.
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta:lista_consultas')
    else:
        # Preenche o formulário com os dados atuais da consulta.
        form = ConsultaForm(instance=consulta)

    return render(request, 'consulta/editar.html', {
        'form': form,
        'titulo': 'Editar consulta'
    })


def excluir_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta:lista_consultas')

    # No GET, só mostra a confirmação; ainda não exclui.
    return render(request, 'consulta/deletar.html', {'consulta': consulta})
