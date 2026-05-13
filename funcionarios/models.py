from django.db import models

class FuncionarioBase(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    formacao = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=14, null=False, blank=False, unique=True)
    data_nascimento = models.DateField(null=False, blank=False)