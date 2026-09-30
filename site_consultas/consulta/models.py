from django.db.models import Model, CharField, DateTimeField, ForeignKey, PROTECT
from pessoa.models import Pessoa
from medico.models import Medico

# Create your models here.

class Consulta(Model):
    dataHora = DateTimeField()
    
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    status = CharField(max_length=20, choices=STATUS_CHOICES)

    pessoa = ForeignKey(Pessoa, on_delete=PROTECT, related_name='consultasPaciente')
    medico = ForeignKey(Medico, on_delete=PROTECT, related_name='consultasMedico')