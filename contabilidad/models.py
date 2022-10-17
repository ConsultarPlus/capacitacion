from django.db import models
from django.core.validators import RegexValidator
from tabla.listas import SINO


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
