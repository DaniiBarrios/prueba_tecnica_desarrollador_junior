from django.contrib import admin
from procesamiento.models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'cholesterol')
