from django.contrib import admin
from alumnos.models import Alumno, Matricula

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_estudiante', 'email')
    search_fields = ('nombre', 'codigo_estudiante', 'email')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'asignacion', 'fecha_matricula', 'estado', 'nota_final')
    list_filter = ('estado',)