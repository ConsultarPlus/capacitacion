from django.db import models
from administracion.models import Moneda
from tabla.models import Tabla
from administracion.models import Departamento


# Create your models here.
class Articulo(models.Model):
    artcod = models.CharField(max_length=13, null=False, blank=False)
    descripcion = models.CharField(max_length=60, null=True, blank=True)
    iva = models.FloatField(max_length=6, null=True, blank=True, default=21)
    precio = models.FloatField(max_length=12, null=True, blank=True)
    moneda = models.ForeignKey(Moneda, null=True, blank=True, on_delete=models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, null=False, blank=False)
    artuniven = models.ForeignKey(Tabla, null=True, blank=True, related_name='UNIDADES', on_delete=models.DO_NOTHING)
    descextra = models.CharField(max_length=255, null=True, blank=True)
    ubicacion = models.CharField(max_length=15, null=True, blank=True)
    artimg = models.FileField(null=True, blank=True)
    marca = models.ForeignKey(Tabla, related_name='marca', on_delete=models.DO_NOTHING, null=True, blank=True)
    color = models.ForeignKey(Tabla, related_name='color', on_delete=models.DO_NOTHING, null=True, blank=True)
    codbar = models.CharField(max_length=30, null=True, blank=True)
