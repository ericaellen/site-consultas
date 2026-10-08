from django.shortcuts import redirect, render
from .forms import EspecialidadeForm, MedicoForm
from .models import Especialidade, Medico

def lista_especialidades(request):
    # Busca todas as especialidades cadastradas para mostrar na lista.
    especialidades = Especialidade.objects.all()
    return render(request, 'medico/especialidades/lista.html', {'especialidades': especialidades})


def adicionar_especialidade(request):
    # Se o formulário foi enviado, usa os dados recebidos para criar a especialidade.
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        # Só salva no banco quando os dados passaram pela validação do ModelForm.
        if form.is_valid():
            form.save()
            # Depois de cadastrar, volta para a lista de especialidades.
            return redirect('lista_especialidades')
    else:
        # Em uma visita normal (GET), exibe um formulário vazio.
        form = EspecialidadeForm()

    # Mostra o formulário vazio ou, se houver erros, o formulário com as mensagens de validação.
    return render(request, 'medico/especialidades/formulario.html', {
        'form': form,
        'titulo': 'Adicionar especialidade'
    })


def detalhar_especialidade(request, id):
    # Busca a especialidade pelo ID recebido na URL.
    especialidade = Especialidade.objects.get(id=id)
    # Envia o registro encontrado ao template para exibir seus dados.
    return render(request, 'medico/especialidades/detalhar.html', {'especialidade': especialidade})


def editar_especialidade(request, id):
    # Busca o registro que será alterado.
    especialidade = Especialidade.objects.get(id=id)
    if request.method == 'POST':
        # Associa os dados enviados ao registro existente, em vez de criar outro.
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            # Depois de editar, volta para a lista.
            return redirect('lista_especialidades')
    else:
        # No GET, mostra o formulário preenchido com os dados atuais.
        form = EspecialidadeForm(instance=especialidade)

    # Exibe o formulário de edição e possíveis erros de validação.
    return render(request, 'medico/especialidades/formulario.html', {
        'form': form,
        'titulo': 'Editar especialidade',
        'especialidade': especialidade
    })


def excluir_especialidade(request, id):
    # Busca o registro que será exibido na página de confirmação.
    especialidade = Especialidade.objects.get(id=id)
    if request.method == 'POST':
        # Só exclui depois que a confirmação é enviada pelo formulário.
        especialidade.delete()
        return redirect('lista_especialidades')

    # No GET, apenas mostra a confirmação; ainda não exclui o registro.
    return render(request, 'medico/especialidades/excluir.html', {'especialidade': especialidade})

#PARTE DE MEDICOS
def lista_medicos(request):
    # Busca os médicos cadastrados para mostrar na lista.
    medicos = Medico.objects.all()
    return render(request, 'medico/lista.html', {'medicos': medicos})


def adicionar_medico(request):
    # No envio do formulário, valida e salva os dados do médico.
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            medico = form.save()
            # Salva também as especialidades escolhidas no formulário.
            medico.especialidades.set(form.cleaned_data['especialidades'])
            return redirect('lista_medicos')
    else:
        # Ao abrir a página, mostra um formulário vazio.
        form = MedicoForm()

    return render(request, 'medico/formulario.html', {
        'form': form,
        'titulo': 'Adicionar médico'
    })


def detalhar_medico(request, id):
    # Busca o médico pelo ID e envia seus dados ao template.
    medico = Medico.objects.get(id=id)
    return render(request, 'medico/detalhar.html', {'medico': medico})


def editar_medico(request, id):
    # Busca o médico que será editado.
    medico = Medico.objects.get(id=id)
    if request.method == 'POST':
        # Usa a instância existente para atualizar, em vez de criar outro médico.
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            medico = form.save()
            # Atualiza as especialidades associadas ao médico.
            medico.especialidades.set(form.cleaned_data['especialidades'])
            return redirect('lista_medicos')
    else:
        # Preenche o formulário com os dados atuais do médico.
        form = MedicoForm(instance=medico)
        form.fields['especialidades'].initial = medico.especialidades.all()

    return render(request, 'medico/formulario.html', {
        'form': form,
        'titulo': 'Editar médico'
    })


def excluir_medico(request, id):
    # Busca o médico que será exibido na confirmação.
    medico = Medico.objects.get(id=id)
    if request.method == 'POST':
        # Consulta protege médicos vinculados, então avisa antes de tentar excluir.
        if medico.consultasMedico.exists():
            return render(request, 'medico/excluir.html', {
                'medico': medico,
                'erro': 'Não é possível excluir este médico porque ele possui consultas.'
            })
        medico.delete()
        return redirect('lista_medicos')

    # No GET, só mostra a confirmação; ainda não exclui.
    return render(request, 'medico/excluir.html', {'medico': medico})
