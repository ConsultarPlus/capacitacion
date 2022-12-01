from django import forms
from django.urls import reverse

from .models import Cliente, Tipos_Iva, CliEma
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder


def maybe_button(id):
    if id is -1:
        return 0
    return Button('emails', 'Emails', css_class='btn-default', onclick="window.location.href = '{}';".format(reverse('cliema_listar', kwargs={'id': id})))


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        try:
            id = kwargs.pop('id')
        except Exception:
            id = -1
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
                Column('telefono', css_class='form-group col-md-3 mb-0'),
                Column('domicilio', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-0'),
                maybe_button(id),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


########################################################################################################################


class Tipos_IvaForm(forms.ModelForm):

    class Meta:
        model = Tipos_Iva
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('codigo_afip', css_class='form-group col-md-3 mb-0'),
                Column('columna_libroiva', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


########################################################################################################################


class CliEmaForm(forms.ModelForm):

    class Meta:
        model = CliEma
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('cliente', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('principal', css_class='form-group col-md-1 mb-2'),
                Column('enviar_factura', css_class='form-group col-md-1 mb-2'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )
