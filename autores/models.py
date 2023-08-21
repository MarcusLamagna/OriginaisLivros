from django.db import models


# Create your models here.
class Telefone(models.Model):
    numero = models.CharField(max_length=13, null=False, blank=False)


class Autores(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='Escolher Sexo')
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    cpf = models.CharField(max_length=15, unique=True, null=False, blank=True)
    foto = models.ImageField(upload_to='fotos_autores', null=False, blank=False)
    telefone = models.OneToOneField(Telefone, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
