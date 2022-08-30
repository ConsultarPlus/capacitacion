from django import forms
from administracion.models import Viajante, Transporte, CondicionDePago
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML
from crispy_forms.bootstrap import FieldWithButtons
from tabla.widgets import SelectLiveSearchInput
from tabla.funcs import boton_buscar
from tabla.gets import get_choices, get_choices_mas_vacio
from tabla.listas import MODELOS, ITEMS_X_PAG, SINO, ACTIVO, PERIODO


class ViajanteForm(forms.ModelForm):

    class Meta:
        model = Viajante
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['codigo'].label = 'Código'
        self.fields['direccion'].label = 'Dirección'
        self.fields['nombre'].label = 'Nombre'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['email'].label = 'Email'
        self.fields['comision_venta'].label = 'Comisión Venta'
        self.fields['comision_cobro'].label = 'Comisión Cobro'
        self.fields['usuario'].label = 'Usuario'
        self.fields['zona'].label = 'Zona'
        self.fields['activo'].widget = SelectLiveSearchInput(choices=ACTIVO)
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('codigo', css_class='form-group col-md-2 mb-0'),
                Column('nombre', css_class='form-group col-md-3 mb-0'),
                Column('telefono', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('direccion', css_class='form-group col-md-5 mb-0'),
                Column('zona', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('usuario', css_class='form-group col-md-3 mb-0'),
                Column('activo', css_class='form-group col-md-1 mb-0'),
            ),
            Row(
                Column('comision_venta', css_class='form-group col-md-4 mb-0'),
                Column('comision_cobro', css_class='form-group col-md-4 mb-0'),

            ),

            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class TransporteForm(forms.ModelForm):

    class Meta:
        model = Transporte
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['nombre'].label = 'Nombre'
        self.fields['direccion'].label = 'Dirección'
        self.fields['cuit'].label = 'Cuit'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['email'].label = 'Email'
        self.fields['web'].label = 'Sitio web'
        self.fields['importe_minimo'].label = 'Importe Mínimo'
        self.fields['porcentaje_valor_carga'].label = 'Porcentaje de Valor de Carga'
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(            Row(
                Column('nombre', css_class='form-group col-md-3 mb-0'),
                Column('cuit', css_class='form-group col-md-2 mb-0'),
                Column('localidad', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('direccion', css_class='form-group col-md-3 mb-0'),
                Column('telefono', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('web', css_class='form-group col-md-3 mb-0'),
                Column('email', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('importe_minimo', css_class='form-group col-md-3 mb-0'),
                Column('porcentaje_valor_carga', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class CondicionDePagoForm(forms.ModelForm):
    class Meta:
        model = CondicionDePago
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['descripcion'].label = 'Descripción'
        self.fields['porcentaje'].label = 'Porcentaje'
        self.fields['cuotas'].label = 'Cuotas'
        self.fields['dia_vencimiento'].label = 'Día de Vencimiento'
        self.fields['periodo_cantidad'].label = 'Cantidad de Periodos'
        self.fields['activo'].widget = SelectLiveSearchInput(choices=ACTIVO)
        self.fields['periodo'].widget = SelectLiveSearchInput(choices=PERIODO)
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('descripcion', css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('porcentaje', css_class='form-group col-md-2 mb-0'),
                Column('cuotas', css_class='form-group col-md-2 mb-0'),
                Column('dia_vencimiento', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('periodo_cantidad', css_class='form-group col-md-3 mb-0'),
                Column('periodo', css_class='form-group col-md-3 mb-0'),
                Column('activo', css_class='form-group col-md-1 mb-0'),
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )