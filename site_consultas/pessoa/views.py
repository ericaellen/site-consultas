from django.db.models.deletion import ProtectedError
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from .forms import PessoaForm
from .models import Pessoa


def index(request):
    # Busca todas as pessoas para mostrar na lista.
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/lista.html', {'pessoas': pessoas})


def detail(request, id):
    # Busca a pessoa pelo ID; se não existir, responde com página não encontrada.
    try:
        pessoa = Pessoa.objects.get(id=id)
    except Pessoa.DoesNotExist:
        return HttpResponseNotFound('Pessoa não encontrada.')

    return render(request, 'pessoa/detalhar.html', {'pessoa': pessoa})


def add(request):
    # No envio, valida os dados antes de salvar a pessoa.
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pessoa/')
    else:
        # Ao abrir a página, mostra um formulário vazio.
        form = PessoaForm()

    return render(request, 'pessoa/formulario.html', {
        'form': form,
        'titulo': 'Adicionar pessoa'
    })


def edit(request, id):
    # Busca a pessoa que será editada.
    try:
        pessoa = Pessoa.objects.get(id=id)
    except Pessoa.DoesNotExist:
        return HttpResponseNotFound('Pessoa não encontrada.')

    if request.method == 'POST':
        # Usa a pessoa existente para atualizar, em vez de criar outra.
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('/pessoa/')
    else:
        # Preenche o formulário com os dados atuais da pessoa.
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoa/formulario.html', {
        'form': form,
        'titulo': 'Editar pessoa'
    })


def delete(request, id):
    # Busca a pessoa que será mostrada na confirmação.
    try:
        pessoa = Pessoa.objects.get(id=id)
    except Pessoa.DoesNotExist:
        return HttpResponseNotFound('Pessoa não encontrada.')

    if request.method == 'POST':
        try:
            pessoa.delete()
        except ProtectedError:
            # O banco impede a exclusão enquanto houver consultas relacionadas.
            return render(request, 'pessoa/deletar.html', {
                'pessoa': pessoa,
                'erro': 'Não é possível excluir esta pessoa porque há consultas vinculadas.'
            })
        return redirect('/pessoa/')

    # No GET, só mostra a confirmação; ainda não exclui.
    return render(request, 'pessoa/deletar.html', {'pessoa': pessoa})


def toList(request):
    # Mantém a rota /list/ exibindo a mesma lista de pessoas.
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/lista.html', {'pessoas': pessoas})
