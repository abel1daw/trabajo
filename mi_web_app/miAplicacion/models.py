from django.db import models
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    fechaNacimiento = models.DateField('Fecha Nacimiento')
class Genero(models.Model):
    nombre = models.CharField(max_length=200, unique=True, help_text="Género del libro")
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.RESTRICT, null=True)
    resumen = models.TextField( max_length=1000, help_text="Introduce un resumen del libro.") 
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='Introduce el ISBN')
    genero = models.ManyToManyField(Genero, help_text="Escoge el género")