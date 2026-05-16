
from rest_framework import viewsets
from .models import *
from .serializer import *

class FuncionarioGerenciaViewSet(viewsets.ModelViewSet):
    queryset = FuncionarioGerencia.objects.all()
    serializer_class = FuncionarioGerenciaSerializer