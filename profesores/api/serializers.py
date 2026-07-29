from rest_framework.serializers import ModelSerializer
from profesores.models import Profesor, Curso

class ProfesorSerializer(ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'