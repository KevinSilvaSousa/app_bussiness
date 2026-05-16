from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class FuncionarioMarketingViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = FuncionarioMarketingModel.objects.all()
    serializer_class = FuncionarioMarketingSerializer