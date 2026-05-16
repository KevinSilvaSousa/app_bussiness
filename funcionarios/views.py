from rest_framework import viewsets
from .models import *
from .serializer import *

class FuncionarioBaseViewSet(viewsets.ModelViewSet):

    queryset = FuncionarioBase.objects.all()
    serializer_class = FuncionarioBaseSerializer

  