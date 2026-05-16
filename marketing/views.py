from rest_framework import viewsets
from .models import *
from .serializer import *


class FuncionarioMarketingViewSet(viewsets.ModelViewSet):
    queryset = FuncionarioMarketing.objects.all()
    serializer_class = FuncionarioMarketingSerializer