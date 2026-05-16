from rest_framework import serializers
from .models import *

class FuncionarioMarketingSerializer(serializers.ModelSerializer):

    class Meta:
        model = FuncionarioMarketingModel
        fields = ['nome', 'funcionario', 'area_atuacao', 'graduacao', 'redes_sociais', 'campanhas_ativas']