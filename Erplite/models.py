from django.db import models


class login(models.Model):

    login = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)

class Colaboradores (models.Model):
    
    nome = models.CharField(max_length=15)
    sobreNome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=12)
    ctps = models.CharField(max_length=15)
    pis = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    complemento = models.CharField(max_length=15)
    numero = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    
    
    