from django.db import models
from funcionarios.models import FuncionarioBase

class FuncionarioTi(models.Model):
    funcionario = models.OneToOneField(FuncionarioBase, on_delete=models.CASCADE, related_name="ti")
    tecnologia = models.CharField(max_length=100)
    graduacao = models.CharField(max_length=50)