import datetime

from django import forms
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Row, Column, Button
from tabla.widgets import DatePickerInput
from bancos.models import CuentaBancaria, Chequera
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG
from tabla.widgets import SelectLiveSearchInput


class FiltroCuentaBancaria(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    items = forms.IntegerField(max_value=30,
                               min_value=5,
                               required=False,
                               label='ítems x pág.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.disable_csrf = True
        self.fields['items'].widget = SelectLiveSearchInput(choices=ITEMS_X_PAG)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'

        self.helper.layout = Layout(
            Row(
                Column('buscar', css_class='form-group col-md-2 mb-0 '),
                FieldWithButtons('items', boton_buscar(), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            )
        )


class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

    emision_fecha = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False,
                                    initial=datetime.date.today().strftime('%d/%m/%Y'))
    acreditacion_fecha = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False,
                                         initial=datetime.date.today().strftime('%d/%m/%Y   '))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        try:
            emision_fecha = kwargs['initial']['emision_fecha']
            self.fields['emision_fecha'].initial = emision_fecha
        except Exception as e:
            pass

        try:
            acreditacion_fecha = kwargs['initial']['acreditacion_fecha']
            self.fields['acreditacion_fecha'].initial = acreditacion_fecha
        except Exception as e:
            pass

        self.helper.layout = Layout(
            Row(
                Column('cuenta', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                Column('banco', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sucursal', css_class='form-group col-md-3 mb-0'),
                Column('titular', css_class='form-group col-md-6 mb-0'),
                Column('emision_fecha', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('emision_saldo', css_class='form-group col-md-3 mb-0'),
                Column('acreditacion_fecha', css_class='form-group col-md-6 mb-0'),
                Column('acreditacion_saldo', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class FiltroChequera(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    items = forms.IntegerField(max_value=30,
                               min_value=5,
                               required=False,
                               label='ítems x pág.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.disable_csrf = True
        self.fields['items'].widget = SelectLiveSearchInput(choices=ITEMS_X_PAG)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'

        self.helper.layout = Layout(
            Row(
                Column('buscar', css_class='form-group col-md-2 mb-0 '),
                FieldWithButtons('items', boton_buscar(), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            )
        )


class ChequeraForm(forms.ModelForm):
    class Meta:
        model = Chequera
        fields = '__all__'

    recibida = forms.DateField(input_formats=['%d/%m/%y'], widget=DatePickerInput(), required=False,
                               initial=datetime.date.today().strftime('%d/%m/%y'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            recibida = kwargs['initial']['recibida']
            self.fields['recibida'].initial = recibida
        except Exception as e:
            pass

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('inactiva', css_class='form-group col-md-3 mb-0'),
                Column('electronica', css_class='form-group col-md-3 mb-0'),
                Column('cuenta_bancaria', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('serie', css_class='form-group col-md-3 mb-0'),
                Column('recibida', css_class='form-group col-md-3 mb-0'),
                Column('cheque_desde', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cheque_hasta', css_class='form-group col-md-4 mb-0'),
                Column('pago_diferido', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dias_diferencia', css_class='form-group col-md-4 mb-0'),
                Column('proximo_numero', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )
