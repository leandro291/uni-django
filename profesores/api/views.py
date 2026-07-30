from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from profesores.models import Profesor, Curso, Asignaciones
from profesores.api.serializers import ProfesorSerializer, CursoSerializer, AsignacionesSerializer

class ProfesorViewSet(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AsignacionesViewSet(generics.ListCreateAPIView):
    serializer_class = AsignacionesSerializer

    def get_queryset(self):
        return Asignaciones.objects.filter(profesor_id=self.kwargs['profesor_pk'])

class AsignacionesCursoViewSet(generics.ListCreateAPIView):
    serializer_class = AsignacionesSerializer

    def get_queryset(self):
        return Asignaciones.objects.filter(curso_id=self.kwargs['curso_pk'])