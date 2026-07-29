from rest_framework.routers import DefaultRouter
from profesores.api.views import ProfesorViewSet, CursoViewSet

router_profesores = DefaultRouter()

router_profesores.register('profesores', ProfesorViewSet, basename='profesor')
router_profesores.register('cursos', CursoViewSet, basename='curso')