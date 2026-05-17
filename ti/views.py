from rest_framework import viewsets

from configs.funcionario_permissions import FuncionarioBasePermission
from .models import *
from .serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class FuncionarioTiViewSets(viewsets.ModelViewSet):
    authentication_classes =[SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, FuncionarioBasePermission]
    
    queryset = FuncionarioTiModel.objects.all()
    serializer_class = FuncionarioTiSerializer