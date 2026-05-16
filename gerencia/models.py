from django.db import models
from funcionarios.models import *

class FuncionarioGerenciaModel(models.Model):
    NIVEIS = (
        ("J", "JUNIOR"),
        ("P", "PLENO"),
        ("S", "SENIOR")
    )
    """Models do Funcionario Gerencia"""
    nome = models.CharField(max_length=100, null=False, blank=False)
    funcionario = models.OneToOneField(FuncionarioBaseModel, on_delete=models.CASCADE)
    setor_responsavel = models.CharField(max_length=100)
    quantidade_equipes = models.IntegerField()
    nivel_hierarquico = models.CharField(max_length=1 ,choices=NIVEIS)