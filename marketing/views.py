from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *

@csrf_exempt
def FuncionarioMarketingView(request, pk=None):
    if request.method == "GET":
        funcionario_marketing = FuncionarioMarketing.objects.all()
        serializer = FuncionarioMarketingSerializer(funcionario_marketing, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FuncionarioMarketingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    if request.method == "GET":

        if pk:
            funcionario = FuncionarioMarketing.objects.get(pk=pk)
            serializer = FuncionarioMarketingSerializer(funcionario)
            return JsonResponse(serializer.data, safe=False)

        funcionario_marketing = FuncionarioMarketing.objects.all()
        serializer = FuncionarioMarketingSerializer(funcionario_marketing, many=True)
        return JsonResponse(serializer.data, safe=False) 