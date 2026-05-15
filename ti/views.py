from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *

@csrf_exempt
def FuncionarioTiView(request, pk=None):
    if request.method == "GET":
        funcionario_ti = FuncionarioTi.objects.all()
        serializer = FuncionarioTiSerializer(funcionario_ti, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FuncionarioTiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    if request.method == "GET":

        if pk:
            funcionario = FuncionarioTi.objects.get(pk=pk)
            serializer = FuncionarioTiSerializer(funcionario)
            return JsonResponse(serializer.data, safe=False)

        funcionario_ti = FuncionarioTi.objects.all()
        serializer = FuncionarioTiSerializer(funcionario_ti, many=True)
        return JsonResponse(serializer.data, safe=False) 