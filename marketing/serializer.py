from rest_framework import serializers
from .models import *

class FuncionarioMarketingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FuncionarioMarketingModel
        fields = ['funcionario', 'area_atuacao', 'redes_sociais', 'campanhas_ativas']