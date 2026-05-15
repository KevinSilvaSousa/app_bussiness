from django.contrib import admin
from django.urls import path
from funcionarios.views import FuncionarioBaseView
from gerencia.views import FuncionarioGerenciaView
from marketing.views import FuncionarioMarketingView
from ti.views import FuncionarioTiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("funcionarios/", FuncionarioBaseView),
    path("funcionarios/<int:pk>/", FuncionarioBaseView),
    path("gerencia/", FuncionarioGerenciaView),
    path("gerencia/<int:pk>/", FuncionarioGerenciaView),
    path("marketing/", FuncionarioMarketingView),
    path("marketing/<int:pk>/", FuncionarioMarketingView),
    path("ti/", FuncionarioTiView),
    path("ti/<int:pk>/", FuncionarioTiView),
]
