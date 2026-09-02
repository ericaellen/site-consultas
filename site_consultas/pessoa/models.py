from django.db.models import Model, CharField, IntegerField, EmailField, DateField

# Create your models here.
class Pessoa(Model):
    nome = CharField(max_length=100)
    nascimento = DateField()
    cpf = CharField(max_length=11)
