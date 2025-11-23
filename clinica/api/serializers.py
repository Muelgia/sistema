from rest_framework import serializers
from .models import Paciente, Consulta

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        # campos do model que vao aparecer no json
        fields = ['id', 'nome_completo', 'cpf', 'email', 'data_nascimento']

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        # campos do model que vao aparecer no json
        fields = ['id', 'paciente', 'medico', 'data_hora', 'descricao_sintomas']