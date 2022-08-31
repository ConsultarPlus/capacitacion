from django.db import models
from tabla.listas import SINO
from tabla.models import Tabla
from capacitacion.settings import MEDIA_ROOT
from django.core.validators import MaxValueValidator, MinValueValidator


class Departamento(models.Model):
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=60, verbose_name='Descripción')
    listas_precios = models.CharField(max_length=1, default="N", choices=SINO)
    utilidad_x_defecto = models.FloatField(blank=True, validators=[MaxValueValidator(100.0), MinValueValidator(0.0)])
    rubro = models.ForeignKey(Tabla, on_delete=models.CASCADE, blank=True)
    actualiza_costos = models.CharField(max_length=2, blank=True)
    imagen = models.ImageField(upload_to=MEDIA_ROOT, blank=True)


"""
PE Nº 33551 - CONSP Versión actual 5.12.02
> DESCRIPCIÓN: Crear ABM de modelo "Departamento"

Campos:

codigo - C(12)
descripcion - C(60)
listas_precios - S/N o boolean
utilidad_x_defecto - N(7.2) (porcentaje)
rubro - ForeignKey(Tabla)
actualiza_costos - C(2)
imagen - ImageField
"""