from rest_framework.viewsets import ModelViewSet
from profesores.models import Profesor, Curso
from profesores.api.serializers import ProfesorSerializer, CursoSerializer

class ProfesorViewSet(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

