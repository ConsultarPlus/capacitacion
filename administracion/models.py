from django.db import models
from tabla.listas import SINO
from tabla.models import Tabla
from capacitacion.settings import MEDIA_ROOT
from django.core.validators import MaxValueValidator, MinValueValidator


class Departamento(models.Model):
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=60, verbose_name='Descripción')
    listas_precios = models.CharField(max_length=1, default="N", choices=SINO)
    utilidad_x_defecto = models.FloatField(null=True, blank=True, validators=[MaxValueValidator(100.0), MinValueValidator(0.0)], default=0.0)
    rubro = models.ForeignKey(Tabla, null=True, on_delete=models.DO_NOTHING, blank=True, related_name='RUBRO', limit_choices_to={'entidad': 'RUBRO'})
    actualiza_costos = models.CharField(max_length=2, blank=True)
    imagen = models.ImageField(upload_to=MEDIA_ROOT, blank=True)


class Deposito(models.Model):
    codigo = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=60, verbose_name='Descripción')
    afecta_stock = models.CharField(max_length=1, default="N", choices=SINO)
    activo = models.CharField(max_length=1, default="N", choices=SINO)
    domicilio = models.CharField(max_length=40, blank=True, null=True)
    telefono = models.CharField(max_length=40, verbose_name='Teléfono', blank=True, null=True)
    externo = models.CharField(max_length=1, default="N", choices=SINO)
    # TODO localidad =  models.ForeignKey(Localidad) (aun no existe localidad)
