from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=140)
    tema = models.CharField(max_length=140)
    texto = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']