from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *

@csrf_exempt
def FuncionarioBaseView(request, pk=None):
    if request.method == "GET":
        funcionario_base = FuncionarioBase.objects.all()
        serializer = FuncionarioBaseSerializer(funcionario_base, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FuncionarioBaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    if request.method == "GET":

        if pk:
            funcionario = FuncionarioBase.objects.get(pk=pk)
            serializer = FuncionarioBaseSerializer(funcionario)
            return JsonResponse(serializer.data, safe=False)

        funcionario_base = FuncionarioBase.objects.all()
        serializer = FuncionarioBaseSerializer(funcionario_base, many=True)
        return JsonResponse(serializer.data, safe=False)