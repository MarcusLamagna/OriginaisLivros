from django.db import models

from autores.models import Autores


# Create your models here.
class Original(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False)
    subtitulo = models.CharField(max_length=255, null=False, blank=False)
    # ForeignKey = relacionamento muitos para um
    autores = models.ForeignKey(Autores, null=False, blank=False, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField()
    original = models.FileField(upload_to='originais/', null=False, blank=False)

    def __str__(self):
        return self.titulo
