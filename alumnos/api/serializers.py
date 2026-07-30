from rest_framework.serializers import ModelSerializer
from alumnos.models import Alumno, Matricula

class AlumnoSerializer(ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
        