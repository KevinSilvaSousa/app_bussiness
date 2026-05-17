from rest_framework import serializers
from .models import *

class FuncionarioTiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioTiModel
        fields = ['funcionario', 'tecnologia']
