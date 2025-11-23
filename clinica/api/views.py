from rest_framework import viewsets, permissions
from .models import Paciente, Consulta
from .serializers import PacienteSerializer, ConsultaSerializer

# viewset cria o crud (get, post, put, delete) automaticamente
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # exige que o usuario esteja autenticado
    permission_classes = [permissions.IsAuthenticated]

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    # exige que o usuario esteja autenticado
    permission_classes = [permissions.IsAuthenticated]
