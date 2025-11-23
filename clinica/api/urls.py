from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router registra as viewsets e cria as urls automaticamente
router = DefaultRouter()
router.register('pacientes', views.PacienteViewSet)
router.register('consultas', views.ConsultaViewSet)

# urls do app api
urlpatterns = [
    path('', include(router.urls)),
]