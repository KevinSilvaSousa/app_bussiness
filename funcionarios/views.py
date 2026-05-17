from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from configs.funcionario_permissions import FuncionarioBasePermission

class FuncionarioBaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, FuncionarioBasePermission]

    queryset = FuncionarioBaseModel.objects.all()
    serializer_class = FuncionarioBaseSerializer

  