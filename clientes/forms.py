from django import forms
from .models import Cliente
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML
from crispy_forms.bootstrap import FieldWithButtons
from tabla.widgets import SelectLiveSearchInput, DatePickerInput
from tabla.listas import ITEMS_X_PAG, SINO
from tabla.funcs import boton_buscar
from datetime import datetime


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('clicod', css_class='form-group col-md-3 mb-0'),
                Column('nombre', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cuit', css_class='form-group col-md-3 mb-0'),
                Column('tipoiva', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('telefono', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('domicilio', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )