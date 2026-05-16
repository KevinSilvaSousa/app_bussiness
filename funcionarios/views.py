from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class FuncionarioBaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = FuncionarioBaseModel.objects.all()
    serializer_class = FuncionarioBaseSerializer

  