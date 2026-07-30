from rest_framework.serializers import ModelSerializer
from profesores.models import Profesor, Curso, Asignaciones

class ProfesorSerializer(ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'especialidad']

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'creditos']

class AsignacionesSerializer(ModelSerializer):
    class Meta:
        model = Asignaciones
        fields = ['id', 'profesor', 'curso', 'periodo_academico', 'seccion', 'capacidad', 'horas_semanales']