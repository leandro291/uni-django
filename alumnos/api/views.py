from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from alumnos.models import Alumno, Matricula
from alumnos.api.serializers import AlumnoSerializer, MatriculaSerializer

class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class MatriculaAlumnoViewSet(generics.ListAPIView):
    serializer_class = MatriculaSerializer

    def get_queryset(self):
        return Matricula.objects.filter(alumno_id=self.kwargs['alumno_pk'])

class MatriculaAsignacionViewSet(generics.ListCreateAPIView):
    serializer_class = MatriculaSerializer

    def get_queryset(self):
        return Matricula.objects.filter(asignacion_id=self.kwargs['asignacion_pk'])