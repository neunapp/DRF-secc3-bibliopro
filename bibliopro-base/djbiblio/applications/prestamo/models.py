from django.db import models
from applications.libro.models import Libro

from .managers import PrestamoManager

# Create your models here.
class Estudiante(models.Model):
    dni = models.CharField('DNI', max_length=10)
    name = models.CharField('Nombres', max_length=25)
    last_name = models.CharField('Apellidos', max_length=25)
    date_birth = models.DateField('Fecha Nacimiento', blank=True, null=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
    
    def __str__(self):
        return self.name + " " + self.last_name


class Prestamo(models.Model):
    book = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE, 
        verbose_name='Libro'
    )
    student = models.ForeignKey(
        Estudiante, 
        on_delete=models.CASCADE, 
        verbose_name='Estudiante'
    )
    description = models.CharField(
        'Descripcion', 
        max_length=100, 
        blank=True,
    )
    date = models.DateField('Fecha Prestamo')
    
    objects = PrestamoManager()
    
    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
    
    def __str__(self):
        return self.book.title + " - " + self.student.name


class Devolucion(models.Model):
    loan = models.ForeignKey(
        Prestamo, 
        on_delete=models.CASCADE, 
        verbose_name='Prestamo'
    )
    date = models.DateField('Fecha Devolucion')
    
    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'
    
    def __str__(self):
        return self.loan.book.title