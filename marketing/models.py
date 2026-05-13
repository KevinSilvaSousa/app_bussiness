from django.db import models
from funcionarios.models import FuncionarioBase


class FuncionarioMarketing(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    funcionario = models.OneToOneField(FuncionarioBase, on_delete=models.CASCADE)
    area_atuacao = models.CharField(max_length=100)
    graduacao = models.CharField(max_length=100)
    redes_sociais = models.CharField(max_length=100)
    campanhas_ativas = models.IntegerField()