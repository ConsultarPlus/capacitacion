from django import forms
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Row, Column, Button
from bancos.models import CuentaBancaria, Chequera, MovBancario, MovBancarios_Detalle
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG, TIPO_MOV_BANCARIO
from tabla.widgets import SelectLiveSearchInput
from tabla.widgets import DatePickerInput


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

    emision_fecha = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    acreditacion_fecha = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)

    def __init__(self, *args, **kwargs):

        try:
            id = kwargs.pop('id')
            initial = kwargs.get('initial', {})
        except Exception as e:
            pass
        try:
            initial['emision_fecha'] = CuentaBancaria.objects.get(pk=id).emision_fecha.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['acreditacion_fecha'] = CuentaBancaria.objects.get(pk=id).acreditacion_fecha.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            kwargs['initial'] = initial
        except Exception as e:
            pass

        super().__init__(*args, **kwargs)

        self.fields['emision_fecha'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['acreditacion_fecha'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('cuenta', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('banco', css_class='form-group col-md-3 mb-0'),
                Column('sucursal', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cuenta_contable', css_class='form-group col-md-3 mb-0'),
                Column('pago_dif', css_class='form-group col-md-3 mb-0'),
                Column('titular', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('emision_fecha', css_class='form-group col-md-3 mb-0'),
                Column('emision_saldo', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('acreditacion_fecha', css_class='form-group col-md-3 mb-0'),
                Column('acreditacion_saldo', css_class='form-group col-md-3 mb-0'),
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

    recibida = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)

    def __init__(self, *args, **kwargs):

        try:
            id = kwargs.pop('id')
            initial = kwargs.get('initial', {})
        except Exception as e:
            pass
        try:
            initial['recibida'] = Chequera.objects.get(pk=id).recibida.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            kwargs['initial'] = initial
        except Exception as e:
            pass

        super().__init__(*args, **kwargs)

        self.fields['recibida'].widget.attrs.update({
            'autocomplete': 'off'
        })
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


class FiltroMovBancario(forms.Form):
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


class MovBancarioForm(forms.ModelForm):
    class Meta:
        model = MovBancario
        fields = '__all__'

    emision = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    vencimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    acreditacion = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)

    def __init__(self, *args, **kwargs):

        initial = kwargs.get('initial', {})
        try:
            usuario = kwargs.pop('user')
            initial['usuario'] = usuario
        except Exception as e:
            pass
        try:
            id = kwargs.pop('id')
        except Exception as e:
            pass
        try:
            initial['emision'] = MovBancario.objects.get(pk=id).emision.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['vencimiento'] = MovBancario.objects.get(pk=id).vencimiento.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['acreditacion'] = MovBancario.objects.get(pk=id).acreditacion.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        kwargs['initial'] = initial
        new_choices = list(kwargs.pop('choices'))

        super().__init__(*args, **kwargs)

        self.fields['tipo'].choices = new_choices
        self.fields['tipo'].widget.choices = new_choices

        self.fields['emision'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['vencimiento'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['acreditacion'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.form_id = 'mov_form'
        self.helper.layout = Layout(
            Row(
                Column('numero', css_class='form-group col-md-3 mb-0'),
                Column('tipo', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cuenta_bancaria', css_class='form-group col-md-3 mb-0'),
                Column('sucursal', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('emision', css_class='form-group col-md-1 mb-0'),
                Column('vencimiento', css_class='form-group col-md-1 mb-0'),
                Column('acreditacion', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('importe', css_class='form-group col-md-2 mb-0'),
                Column('cotizacion', css_class='form-group col-md-2 mb-0'),
                Column('moneda', css_class='form-group col-md-1  mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('concepto_bancario', css_class='form-group col-md-3 mb-0'),
                Column('clearing', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('observacion', css_class='form-group col-md-3 mb-0'),
                Column('nro_conciliacion', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('id_asociado', css_class='form-group col-md-3 mb-0'),
                Column('transferido', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('chepro_anulado', css_class='form-group col-md-3 mb-0'),
                Column('lote', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('usuario', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar movimiento', css_id='movSubmit'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class MovBancarios_DetalleForm(forms.ModelForm):
    class Meta:
        model = MovBancarios_Detalle
        fields = '__all__'

    vencimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)

    def __init__(self, *args, **kwargs):

        initial = kwargs.get('initial', {})
        try:
            id = kwargs.pop('id')
        except Exception as e:
            pass
        try:
            initial['vencimiento'] = MovBancarios_Detalle.objects.get(pk=id).vencimiento.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

        self.fields['vencimiento'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.form_id = 'detalles_form'
        self.helper.layout = Layout(
            Row(
                Column('medio_pago', css_class='form-group col-md-1 mb-0'),
                Column('cheque', css_class='form-group col-md-1 mb-0'),
                Column('importe', css_class='form-group col-md-1 mb-0'),
                Column('vencimiento', css_class='form-group col-md-1 mb-0'),
                Column('cheque_numero', css_class='form-group col-md-1 mb-0'),
                Column('estado_anterior', css_class='form-group col-md-1 mb-0'),
                Submit('submit', 'Grabar detalle', css_id="detallesSubmit"),
                css_class='form-row'
            ),
        )