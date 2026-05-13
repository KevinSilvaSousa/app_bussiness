from django.contrib import admin
from django.urls import path
from funcionarios.views import FuncionarioBaseView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("funcionarios/", FuncionarioBaseView),
    path("funcionarios/<int:pk>/", FuncionarioBaseView),
]
