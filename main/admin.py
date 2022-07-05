from django.contrib import admin

from main.models import Paciente, Exame


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'endereco',)

    list_filter = ('nome', 'idade', 'endereco',)

    search_fields = ('nome', 'idade', 'endereco',)


@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome_prof', 'data_exame', 'peso', 'altura', 'paciente')

    list_filter = ('nome_prof', 'data_exame', 'peso', 'altura', 'paciente')

    search_fields = ('nome_prof', 'data_exame', 'peso', 'altura', 'paciente')
