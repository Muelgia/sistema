from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    # campos da tabela paciente
    nome_completo = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome_completo

class Consulta(models.Model):
    # campos da tabela consulta
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    descricao_sintomas = models.TextField(blank=True)
    
    link_telemedicina = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Consulta de {self.paciente.nome_completo} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
    

