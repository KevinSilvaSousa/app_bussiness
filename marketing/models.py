from django.db import models
from funcionarios.models import FuncionarioBaseModel


class FuncionarioMarketingModel(models.Model):
    funcionario = models.OneToOneField(FuncionarioBaseModel, on_delete=models.CASCADE)
    area_atuacao = models.CharField(max_length=100)
    redes_sociais = models.CharField(max_length=100)
    campanhas_ativas = models.IntegerField()