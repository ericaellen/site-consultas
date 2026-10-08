from django.db.models import Model, CharField, EmailField, DateField

# Create your models here.
class Pessoa(Model):
    nome = CharField(max_length=100)
    nascimento = DateField()
    cpf = CharField(max_length=11, unique=True)
    telefone = CharField(max_length=15, default= "S/N")
    email = EmailField(unique=True)

    def __str__(self):
        return self.nome