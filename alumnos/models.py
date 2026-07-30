from django.db import models
from profesores.models import Asignaciones

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    asignaciones = models.ManyToManyField(
        Asignaciones,
        through='Matricula',
        related_name='alumnos'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "alumnos"
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

class Matricula(models.Model):

    class Estado(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'
        PENDIENTE = 'pendiente', 'Pendiente'

    alumno = models.ForeignKey(
        Alumno, 
        on_delete=models.CASCADE,
        related_name='matriculas'
        )
    
    asignacion = models.ForeignKey(
        Asignaciones, 
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    fecha_matricula = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.alumno.nombre} - {self.asignacion.curso.nombre} - {self.asignacion.periodo_academico}"
    
    class Meta:
        db_table = "matriculas"
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        constraints = [
            models.UniqueConstraint(
                fields=['alumno', 'asignacion'],
                name='unique_alumno_asignacion'
            )
        ]
