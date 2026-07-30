from rest_framework.serializers import ModelSerializer
from alumnos.models import Alumno, Matricula

class AlumnoSerializer(ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id', 'nombre', 'codigo_estudiante', 'email']

class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'alumno', 'asignacion', 'fecha_matricula', 'estado', 'nota_final']
        read_only_fields = ['fecha_matricula']
