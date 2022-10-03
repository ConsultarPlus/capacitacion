from django.db import models
from contabilidad.models import PlanDeCuentas
from perfiles.models import Perfil
from administracion.models import MedioDePago
from django.template import defaultfilters


class Caja(models.Model):
    codigo = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    cuenta_contable = models.ForeignKey(PlanDeCuentas, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descripcion


class CajaCierres(models.Model):
    numero = models.AutoField(primary_key=True, unique=True, null=False)
    saldo_apertura_anterior = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    saldo_cierre_anterior = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    saldo_cheques = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    saldo_apertura = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    cierre = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.DO_NOTHING)
    caja = models.ForeignKey(Caja, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(f"{self.numero}")


class CierresMedio(models.Model):
    medio_de_pago = models.ForeignKey(MedioDePago, null=True, blank=True, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    cuenta_contable = models.ForeignKey(PlanDeCuentas, null=True, blank=True, on_delete=models.DO_NOTHING)
    caja_cierre = models.ForeignKey(CajaCierres, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.descripcion


