from rest_framework.permissions import BasePermission
from funcionarios.models import *
    

class FuncionarioBasePermission(BasePermission):
    message = 'Verificação de Funcionario ...'

    def has_permission(self, request, view):
        funcionario_banco = request.user.id
        blocked = FuncionarioBaseModel.objects.filter(id=funcionario_banco).exists()
        return  blocked
