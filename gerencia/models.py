from django.db import models
from funcionarios.models import *

class FuncionarioGerenciaModel(models.Model):
    """Models do Funcionario Gerencia"""
    funcionario = models.ForeignKey(FuncionarioBaseModel, on_delete=models.CASCADE)
    setor_responsavel = models.CharField(max_length=100)
    quantidade_equipes = models.IntegerField()