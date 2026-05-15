from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *

@csrf_exempt
def FuncionarioGerenciaView(request, pk=None):
    if request.method == "GET":
        funcionario_gerencia = FuncionarioGerencia.objects.all()
        serializer = FuncionarioGerenciaSerializer(funcionario_gerencia, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FuncionarioGerenciaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    if request.method == "GET":

        if pk:
            funcionario = FuncionarioGerencia.objects.get(pk=pk)
            serializer = FuncionarioGerenciaSerializer(funcionario)
            return JsonResponse(serializer.data, safe=False)

        funcionario_gerencia = FuncionarioGerencia.objects.all()
        serializer = FuncionarioGerenciaSerializer(funcionario_gerencia, many=True)
        return JsonResponse(serializer.data, safe=False) 