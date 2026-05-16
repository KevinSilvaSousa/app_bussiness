from django.db import models
from funcionarios.models import FuncionarioBaseModel

class FuncionarioTiModel(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    funcionario = models.OneToOneField(FuncionarioBaseModel, on_delete=models.CASCADE, related_name="ti")
    tecnologia = models.CharField(max_length=100)
    graduacao = models.CharField(max_length=50)