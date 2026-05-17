from rest_framework.permissions import BasePermission
from funcionarios.models import FuncionarioBaseModel 

class FuncionarioBasePermission(BasePermission):
    message = 'Acesso negado. Usuário não identificado como funcionário ativo.'

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        if request.user.is_superuser:
            return True
        
        return FuncionarioBaseModel.objects.filter(id=request.user.id).exists()
    
