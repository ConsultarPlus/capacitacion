from datetime import datetime
from django.db import models
from tabla.models import Tabla
from tabla.listas import SINO


class CuentaBancaria(models.Model):
    cuenta = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=60, null=True, blank=True)
    banco = models.ForeignKey(Tabla, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='BANCO',
                              limit_choices_to={'entidad': 'BANCO'})
    sucursal = models.CharField(max_length=60, null=True, blank=True)
    titular = models.CharField(max_length=60, null=True, blank=True)
    emision_fecha = models.DateField(null=True, blank=True, default=datetime.now().strftime("%d/%m/%Y"))
    emision_saldo = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    acreditacion_fecha = models.DateField(null=True, blank=True, default=datetime.now().strftime("%d/%m/%Y"))
    acreditacion_saldo = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.cuenta


class Chequera(models.Model):
    inactiva = models.CharField(max_length=1, default="N", choices=SINO)
    electronica = models.CharField(max_length=1, default="N", choices=SINO)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, null=True, blank=True, on_delete=models.DO_NOTHING)
    serie = models.CharField(max_length=12, null=True, blank=True)
    recibida = models.DateField(null=True, blank=True, default=datetime.now().strftime("%d/%m/%Y"))
    cheque_desde = models.IntegerField(max_length=8, null=True, blank=True)
    cheque_hasta = models.IntegerField(max_length=8, null=True, blank=True)
    pago_diferido = models.CharField(max_length=1, default="N", choices=SINO)
    dias_diferencia = models.IntegerField(max_length=4, null=True, blank=True)
    proximo_numero = models.IntegerField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.serie

