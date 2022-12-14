from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from administracion.models import Moneda, MedioDePago
from contabilidad.models import PlanDeCuentas
from localidades.models import Localidad
from perfiles.models import Perfil
from tabla.models import Tabla
from tabla.listas import SINO, TIPO_MOV_BANCARIO, ESTADO


class CuentaBancaria(models.Model):
    cuenta = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=60, null=True, blank=True)
    banco = models.ForeignKey(Tabla, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='BANCO',
                              limit_choices_to={'entidad': 'BANCO'})
    sucursal = models.CharField(max_length=60, null=True, blank=True)
    titular = models.CharField(max_length=60, null=True, blank=True)
    moneda = models.ForeignKey(Moneda, null=True, blank=True, on_delete=models.DO_NOTHING)
    cuenta_contable = models.ForeignKey(PlanDeCuentas, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="cuenta_contable_fkcc")
    pago_dif = models.ForeignKey(PlanDeCuentas, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="pago_dif_fkcc")
    emision_fecha = models.DateField(null=True, blank=True)
    emision_saldo = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    acreditacion_fecha = models.DateField(null=True, blank=True)
    acreditacion_saldo = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.cuenta


class Chequera(models.Model):
    inactiva = models.CharField(max_length=1, default="N", choices=SINO)
    electronica = models.CharField(max_length=1, default="N", choices=SINO)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, null=True, blank=True, on_delete=models.DO_NOTHING)
    serie = models.CharField(max_length=12)
    recibida = models.DateField(null=True, blank=True)
    cheque_desde = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(99999999), MinValueValidator(0)])
    cheque_hasta = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(99999999), MinValueValidator(0)])
    pago_diferido = models.CharField(max_length=1, default="N", choices=SINO)
    dias_diferencia = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999), MinValueValidator(0)])
    proximo_numero = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(99999999), MinValueValidator(0)])

    def __str__(self):
        return self.serie


class MovBancario(models.Model):
    tipo = models.CharField(max_length=2, default='CR', choices=TIPO_MOV_BANCARIO, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="mov_bancario_fkcb")
    emision = models.DateField(null=True, blank=True)
    vencimiento = models.DateField(null=True, blank=True)
    acreditacion = models.DateField(null=True, blank=True)
    importe = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    concepto_bancario = models.ForeignKey(Tabla, null=True, blank=True, on_delete=models.DO_NOTHING,
                                          related_name='conceptos_bancarios',
                                          limit_choices_to={'entidad': 'CONCEPTOS_BANCARIOS'})
    clearing = models.IntegerField(null=True, blank=True)
    observacion = models.CharField(max_length=60, null=True, blank=True)
    nro_conciliacion = models.IntegerField(null=True, blank=True)
    id_asociado = models.IntegerField(null=True, blank=True)
    usuario = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.DO_NOTHING)
    cotizacion = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    transferido = models.CharField(max_length=12, null=True, blank=True)
    chepro_anulado = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    sucursal = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {str(self.tipo)} {str(self.numero)}"


class MovBancarios_Detalle(models.Model):
    mov_bancario = models.ForeignKey(MovBancario, on_delete=models.DO_NOTHING)
    medio_pago = models.ForeignKey(MedioDePago, null=True, blank=True, on_delete=models.DO_NOTHING)
    cheque = models.IntegerField(null=True, blank=True, default=None)
    importe_det = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, default=None)
    vencimiento_det = models.DateField(null=True, blank=True, default=None)
    cheque_numero = models.IntegerField(null=True, blank=True, default=None)
    estado_anterior = models.CharField(max_length=1, null=True, blank=True, default=None)


class Cheques_Terceros(models.Model):
    importe = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    vencimiento = models.DateField(null=True, blank=True)
    banco = models.ForeignKey(Tabla, null=True, on_delete=models.DO_NOTHING, blank=True, related_name='CHEQUET_BANCO',
                              limit_choices_to={'entidad': 'BANCO'})
    sucursal = models.CharField(max_length=3, null=True, blank=True)
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.DO_NOTHING)
    numero = models.IntegerField(null=True, blank=True)
    clearing = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(99), MinValueValidator(-99)])
    acreditacion = models.DateField(null=True, blank=True)
    ingreso = models.DateField(null=True, blank=True)
    egreso = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=1, default='A', choices=ESTADO, blank=True, null=True)
    endosado = models.CharField(max_length=1, default='N', choices=SINO, blank=True, null=True)
    observacion = models.CharField(max_length=60, blank=True, null=True)
    asociado_ingreso = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="ing")
    asociado_egreso = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="eg")
    librador = models.CharField(max_length=60, blank=True, null=True)
    librador_cuit = models.CharField(max_length=13, blank=True, null=True)
    caja = models.CharField(max_length=1, blank=True, null=True)  # FK(Caja)?
    a_la_orden = models.CharField(max_length=1, default='N', choices=SINO, blank=True, null=True)
    imputado_difcot = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    marcha_rechazado = models.IntegerField(blank=True, null=True)
    debcre = models.ForeignKey(MovBancario, null=True, blank=True, on_delete=models.DO_NOTHING)
    cuenta_nro = models.CharField(max_length=15, blank=True, null=True)
    electronico = models.CharField(max_length=1, default='N', choices=SINO, blank=True, null=True)


class Cheques_Propios(models.Model):
    numero = models.IntegerField(null=True, blank=True)
    chequera = models.ForeignKey(Chequera, on_delete=models.DO_NOTHING, null=True, blank=True)
    emision = models.DateField(null=True, blank=True)
    vencimiento = models.DateField(null=True, blank=True)
    acreditacion = models.DateField(null=True, blank=True)
    importe = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    observacion = models.CharField(max_length=100, null=True, blank=True)
    # cliente = models.ForeignKey(Cliente)
    entregado_a = models.CharField(max_length=60, null=True, blank=True)
    estado = models.CharField(max_length=1, default='A', choices=ESTADO, blank=True, null=True)
    depositado = models.CharField(max_length=8, null=True, blank=True)
    asociado_id = models.IntegerField(null=True, blank=True)
    caja_nro = models.IntegerField(null=True, blank=True)
    caja_tipo = models.CharField(max_length=1, null=True, blank=True)
    nro_conciliacion = models.IntegerField(null=True, blank=True)
    # asiento_pago_diferido = models.ForeignKey(Asientos)
    lote = models.IntegerField(null=True, blank=True)

