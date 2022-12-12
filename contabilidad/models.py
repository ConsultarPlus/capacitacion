from django.db import models
from django.core.validators import RegexValidator
from tabla.listas import SINO
from administracion.models import Moneda
from django.contrib.auth.models import User
from tabla.models import Tabla


class PlanDeCuentas(models.Model):
    cuenta_contable = models.CharField(max_length=15,                   # 0.0.0.0.0 / 00.00.00.00.00 / 000.000.000.000.000
                                       validators=[RegexValidator(r'^\d{1,3}(\.\d{1,3}(\.\d{1,3}(\.\d{1,3}(\.\d{1,3}?)?)?)?)?$')],
                                       help_text='(0.0.00.00.00)',
                                       unique=True)
    descripcion = models.CharField(max_length=60)
    desglosable = models.CharField(max_length=1, default="N", choices=SINO)
    monetaria = models.CharField(max_length=1, default="N", choices=SINO)
    observacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.descripcion


class Ejercicio(models.Model):
    ejercicio = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.CharField(max_length=60, null=False, blank=False)
    fecha_desde = models.DateField(null=False, blank=False)
    fecha_hasta = models.DateField(null=False, blank=False)


ENTIDAD = (
    ('C', 'cuentas'),
    ('S', 'stock'),
    ('B', 'banco'),
    ('CH', 'cheques'),
)


class Asientos(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    orden = models.IntegerField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    observacion = models.TextField(null=False, blank=False)
    fecha_movimiento = models.DateField(null=False, blank=False)
    asociado_id = models.IntegerField(null=False, blank=False)
    asociado_entidad = models.CharField(max_length=50, choices=ENTIDAD, null=False, blank=False)
    provisorio = models.CharField(max_length=1, choices=SINO, null=True, blank=True)
    manual = models.CharField(max_length=1, choices=SINO, null=True, blank=True)
    redondeo_haber = models.FloatField(null=False, blank=False)
    redondeo_debe = models.FloatField(null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='USUARIO', null=True, blank=True, default=User)
    fecha_creacion = models.DateField(null=False, blank=False)
    lote = models.FloatField(null=False, blank=False)


class AsientosDetalle(models.Model):
    asientos = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=Asientos)
    orden = models.FloatField(null=False, blank=False)
    plan_de_cuentas = models.ForeignKey(PlanDeCuentas, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(null=False, blank=False)
    concepto = models.ForeignKey(Tabla, on_delete=models.DO_NOTHING, related_name='CONCEPTO_CONTABLE', null=True, blank=True)
    debe = models.FloatField(null=False, blank=False)
    haber = models.FloatField(null=False, blank=False)
    concepto_costo = models.FloatField(null=False, blank=False)
