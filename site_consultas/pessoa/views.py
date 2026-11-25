from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PessoaForm
from .models import Pessoa


def lista_pessoas(request):
    # Busca todas as pessoas para mostrar na lista.
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/lista.html', {'pessoas': pessoas})


def detalhar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoa/detalhar.html', {'pessoa': pessoa})


def adicionar_pessoa(request):
    # No envio, valida os dados antes de salvar a pessoa.
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa:lista_pessoas')
    else:
        # Ao abrir a página, mostra um formulário vazio.
        form = PessoaForm()

    return render(request, 'pessoa/formulario.html', {
        'form': form,
        'titulo': 'Adicionar pessoa'
    })


def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        # Usa a pessoa existente para atualizar, em vez de criar outra.
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa:lista_pessoas')
    else:
        # Preenche o formulário com os dados atuais da pessoa.
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoa/formulario.html', {
        'form': form,
        'titulo': 'Editar pessoa'
    })


def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        try:
            pessoa.delete()
        except ProtectedError:
            # O banco impede a exclusão enquanto houver consultas relacionadas.
            return render(request, 'pessoa/deletar.html', {
                'pessoa': pessoa,
                'erro': 'Não é possível excluir esta pessoa porque há consultas vinculadas.'
            })
        return redirect('pessoa:lista_pessoas')

    # No GET, só mostra a confirmação; ainda não exclui.
    return render(request, 'pessoa/deletar.html', {'pessoa': pessoa})
