from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)

    class Meta:
        db_table = 'profesores'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    creditos = models.IntegerField()
    profesores = models.ManyToManyField(
        Profesor,
        through='Asignaciones',
        related_name='cursos'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class Asignaciones(models.Model):

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo_academico = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    horas_semanales = models.IntegerField()

    class Meta:
        db_table = 'asignaciones'
        verbose_name = 'Asignación'
        verbose_name_plural = 'Asignaciones'

        constraints = [
            models.UniqueConstraint(
                fields=['profesor', 'curso', 'periodo_academico', 'seccion'],
                name='unique_profesor_curso_periodo_seccion'
            )
        ]

    def __str__(self):
        return f"{self.profesor.nombre} - {self.curso.nombre} - {self.periodo_academico} - {self.seccion}"
