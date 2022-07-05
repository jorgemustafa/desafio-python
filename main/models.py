from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Exame(models.Model):
    nome_prof = models.CharField(max_length=200)
    data_exame = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Exame do {self.paciente}'
