from django.db.models import Model, CharField, ForeignKey, ManyToManyField, CASCADE
from pessoa.models import Pessoa

# Create your models here.
class Especialidade(Model):
    nome = CharField(max_length=100)

class Medico(Pessoa):
    crm = CharField(max_length=20)
    especialidades = ManyToManyField(
        Especialidade, #aqui foi criada a relação de medico com especialidade
        through='MedicoEspecialidade', #o trough me da o controle dessa tabela pelo model
        related_name='medicos' #como acessarei essa lista de emdicos pela especialidade
    )

class MedicoEspecialidade(Model):
    medico = ForeignKey(Medico, on_delete=CASCADE)
    especialidade = ForeignKey(Especialidade, on_delete=CASCADE)