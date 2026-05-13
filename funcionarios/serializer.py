from rest_framework import serializers
from .models import *

class FuncionarioBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioBase
        fields = ["nome", "formacao", "email", "telefone", "data_nascimento"]