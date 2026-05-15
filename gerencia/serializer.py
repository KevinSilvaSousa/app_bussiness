from rest_framework import serializers
from .models import *

class FuncionarioGerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioGerencia
        fields = ["nome", "funcionario", "setor_responsavel", "quantidade_equipes", "nivel_hierarquico"]