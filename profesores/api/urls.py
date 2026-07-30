from rest_framework.routers import DefaultRouter
from profesores.api.views import ProfesorViewSet, CursoViewSet, AsignacionesProfesorListCreate, AsignacionesCursoListCreate
from django.urls import path, include

router_profesores = DefaultRouter()

router_profesores.register('profesores', ProfesorViewSet, basename='profesor')
router_profesores.register('cursos', CursoViewSet, basename='curso')

urlpatterns = [
    path('', include(router_profesores.urls)),
    path('profesores/<int:profesor_pk>/asignaciones/', AsignacionesProfesorListCreate.as_view(), name='asignaciones'),
    path('cursos/<int:curso_pk>/asignaciones/', AsignacionesCursoListCreate.as_view(), name='asignaciones-curso'),
]