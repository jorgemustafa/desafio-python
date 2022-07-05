from rest_framework import viewsets

from main.models import Paciente, Exame
from main.serializers import PacienteSerializer, ExameSerializer


class PacientesViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()


class ExamesViewSet(viewsets.ModelViewSet):
    serializer_class = ExameSerializer
    queryset = Exame.objects.all()
