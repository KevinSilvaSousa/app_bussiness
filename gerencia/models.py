from django.db import models
from funcionarios.models import FuncionarioBase

class FuncionarioGerencia(models.Model):
    NIVEIS = (
        ("J", "JUNIOR"),
        ("P", "PLENO"),
        ""
    )
    """Models do Funcionario Gerencia"""
    funcionario = models.OneToOneField(FuncionarioBase, on_delete=models.CASCADE)
    setor_responsavel = models.CharField(max_length=100)
    quantidade_equipes = models.IntegerField()
    nivel_hierarquico = models.CharField()