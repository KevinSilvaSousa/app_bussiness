from rest_framework import viewsets
from .models import *
from .serializer import *


class FuncionarioTiViewSets(viewsets.ModelViewSet):
    queryset = FuncionarioTi.objects.all()
    serializer_class = FuncionarioTiSerializer