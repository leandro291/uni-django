from django.contrib import admin
from profesores.models import Profesor, Curso, Asignaciones

# Register your models here.
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especialidad',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos',)

@admin.register(Asignaciones)
class AsignacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'profesor', 'curso', 'periodo_academico', 'seccion', 'capacidad', 'horas_semanales',)