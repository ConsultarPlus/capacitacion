from django.db import models
from tabla.models import Tabla
from tabla.listas import SINO
from django.contrib.auth.models import User


class Viajante(models.Model):
    codigo = models.CharField(max_length=5, null=False, blank=False)
    nombre = models.CharField(max_length=60, null=False, blank=False)
    direccion = models.CharField(max_length=80, null=False, blank=False)
    telefono = models.CharField(max_length=60, null=False, blank=False)
    email = models.CharField(max_length=80, null=False, blank=False)
    comision_venta = models.FloatField(null=False, blank=False)
    comision_cobro = models.FloatField(null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=User)
    zona = models.ForeignKey(Tabla, on_delete=models.DO_NOTHING, related_name='ZONA', null=True, blank=True)
    activo = models.CharField(max_length=1, choices=SINO, null=True, blank=True)


PERIODO = (
    ('D', 'dias'),
    ('M', 'meses'),
    ('A', 'años'),
    ('S', 'semanas'),
)


class CondicionDePago(models.Model):
    descripcion = models.CharField(max_length=60, null=False, blank=False)
    dia_vencimiento = models.CharField(max_length=1, null=False, blank=False)
    porcentaje = models.FloatField(null=False, blank=False)
    activo = models.CharField(max_length=1, choices=SINO, null=True, blank=True)
    cuotas = models.IntegerField(null=False, blank=False)
    periodo = models.CharField(max_length=1, choices=PERIODO, null=False, blank=False)
    periodo_cantidad = models.IntegerField(null=False, blank=False)


class Transporte(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)
    direccion = models.CharField(max_length=60, null=False, blank=False)
    cuit = models.CharField(max_length=13, null=False, blank=False)
    telefeno = models.CharField(max_length=60, null=False, blank=False)
    email = models.CharField(max_length=80, null=False, blank=False)
    web = models.CharField(max_length=60, null=False, blank=False)
    localidad = models.ForeignKey(Tabla, on_delete=models.DO_NOTHING, related_name='LOCALIDAD', null=True, blank=True)
    importe_minimo = models.FloatField(null=False, blank=False)
    porcentaje_valor_carga = models.FloatField(null=False, blank=False)
