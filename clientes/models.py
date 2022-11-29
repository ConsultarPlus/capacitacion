from django.db import models
from django.utils.translation import ugettext as _
from articulos.models import Articulo

# Create your models here.
# from tabla.listas import IVAS


class Cliente(models.Model):
    clicod = models.CharField(max_length=5, verbose_name='Código', null=False, blank=False)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    cuit = models.CharField(max_length=13, null=True, blank=True)
    domicilio = models.CharField(max_length=60, null=True, blank=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=60, null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail', max_length=60, null=True, blank=True)
    encriptado = models.CharField(max_length=10, null=True, blank=True)
    # tipoiva = models.CharField(max_length=60, default='I', choices=IVAS)
    saldo_inicial = models.FloatField(max_length=12, null=True, blank=True)
    fecha_saldo = models.DateField(null=True, blank=True)

    def _get_tipocmp(self):
        if self.tipoiva == "A":
            return "01"
        else:
            if self.tipoiva == "B":
                return "06"
            else:
                return "Undefined"

    tipocmp = property(_get_tipocmp)

    def _get_mail_principal(self):
        try:
            principal = CliEma.objects.filter(cliente=self, principal=True).values('email')[0]
            email_principal = principal['email']
        except Exception as e:
            email_principal = None
        return email_principal

    email_principal = property(_get_mail_principal)

    def __str__(self):
        return "{}".format(self.clicod)

    class Meta:
        permissions = (("clientes.cliente_agregar", _("Agregar")),
                       ("clientes.cliente_editar", _("Editar")),
                       ("clientes.cliente_eliminar", _("Eliminar")),
                       ("clientes.puede_listar", _("Listar")),
                       )


class CliEma(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=False, blank=False)
    email = models.EmailField(verbose_name='E-mail', max_length=100, null=True, blank=True)
    principal = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=60, null=True, blank=True)
    enviar_factura = models.BooleanField(default=True)
