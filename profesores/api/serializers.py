from rest_framework.serializers import ModelSerializer
from profesores.models import Profesor, Curso, Asignaciones

class ProfesorSerializer(ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AsignacionesSerializer(ModelSerializer):
    class Meta:
        model = Asignaciones
        fields = '__all__'