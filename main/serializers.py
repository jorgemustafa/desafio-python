from rest_framework import serializers

from main.models import Paciente, Exame


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'
