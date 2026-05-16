from rest_framework import serializers
from .models import *

class FuncionarioGerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioGerenciaModel
        fields = ["nome", "funcionario", "setor_responsavel", "quantidade_equipes", "nivel_hierarquico"]