from django import forms
from django.forms import ModelForm
from .models import Medico, Especialidade


class MedicoForm(ModelForm):
    especialidades = forms.ModelMultipleChoiceField(
        queryset=Especialidade.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta:
        model = Medico
        fields = ['nome', 'nascimento', 'cpf', 'telefone', 'email', 'crm']


class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome']