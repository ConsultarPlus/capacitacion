from django import forms
from administracion.models import Viajante
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML
from crispy_forms.bootstrap import FieldWithButtons
from tabla.widgets import SelectLiveSearchInput
from tabla.funcs import boton_buscar
from tabla.gets import get_choices, get_choices_mas_vacio
from tabla.listas import MODELOS, ITEMS_X_PAG, SINO, ACTIVO


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
