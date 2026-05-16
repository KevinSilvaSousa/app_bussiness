from django.contrib import admin
from django.urls import path, include
from funcionarios.views import FuncionarioBaseViewSet
from gerencia.views import FuncionarioGerenciaViewSet
from marketing.views import FuncionarioMarketingViewSet
from ti.views import FuncionarioTiViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("funcionarios", FuncionarioBaseViewSet)
router.register("gerencia", FuncionarioGerenciaViewSet)
router.register("marketing", FuncionarioMarketingViewSet)
router.register("ti", FuncionarioTiViewSets)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]
