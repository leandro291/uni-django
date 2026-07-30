from rest_framework.routers import DefaultRouter
from django.urls import path, include
from alumnos.api.views import AlumnoViewSet, MatriculaAlumnoViewSet, MatriculaAsignacionViewSet

router_alumnos = DefaultRouter()
router_alumnos.register('alumnos', AlumnoViewSet, basename='alumno')

urlpatterns = [
    path('', include(router_alumnos.urls)),
    path('alumnos/<int:alumno_pk>/matriculas/', MatriculaAlumnoViewSet.as_view(), name='matriculas-alumno'),
    path('asignaciones/<int:asignacion_pk>/matriculas/', MatriculaAsignacionViewSet.as_view(), name='matriculas-asignacion'),
]