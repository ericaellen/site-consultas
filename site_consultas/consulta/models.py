from django.db.models import Model, CharField, DateTimeField

# Create your models here.

class Consulta(Model):
    dataHora = DateTimeField()
    
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    status = CharField(max_length=20, choices=STATUS_CHOICES)