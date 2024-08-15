from django.db import models

# Create your models here.
class paginas(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    fecha_creacion = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre
