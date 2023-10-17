from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    tipologin = models.IntegerField(choices=[(1, 'Administrador'), (2, 'Padrinho'), (3, 'Voluntário')], default=1)