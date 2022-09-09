from django.db import models
from tabla.listas import SINO
from django.core.validators import MaxValueValidator, MinValueValidator


class Pais(models.Model):
    codigo = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=60, verbose_name="Descripción")
    siap = models.CharField(null=True, blank=True, max_length=3)

    def __str__(self):
        return self.descripcion


class Provincia(models.Model):
    codigo = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=60, verbose_name="Descripción")
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, null=True, blank=True)
    cuenta_contable = models.CharField(max_length=10, null=True, blank=True)
    inscripto_ib = models.CharField(max_length=1, default="N", choices=SINO)
    vencimiento_inscripcion = models.DateField(null=True, blank=True, verbose_name="Vencimiento de la inscripción")
    alicuota = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.descripcion


class Localidad(models.Model):
    codigo_postal = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=60)
    caracteristica_telefonica = models.CharField(null=True, blank=True, max_length=5)
    provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.descripcion
