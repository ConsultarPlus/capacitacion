from datetime import date
from django import forms
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Row, Column, Button
from bancos.models import CuentaBancaria, Chequera, MovBancario, MovBancarios_Detalle, Cheques_Terceros, Cheques_Propios
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
                css_class='form-row'
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('banco', css_class='form-group col-md-3 mb-0'),
                Column('sucursal', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('moneda', css_class='form-group col-md-3 mb-0'),
                Column('titular', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cuenta_contable', css_class='form-group col-md-3 mb-0'),
                Column('pago_dif', css_class='form-group col-md-3 mb-0'),
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
                Column('inactiva', css_class='form-group col-md-1 mb-0'),
                Column('electronica', css_class='form-group col-md-1 mb-0'),
                Column('cuenta_bancaria', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('serie', css_class='form-group col-md-2 mb-0'),
                Column('recibida', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cheque_desde', css_class='form-group col-md-2 mb-0'),
                Column('cheque_hasta', css_class='form-group col-md-2 mb-0'),
                Column('proximo_numero', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pago_diferido', css_class='form-group col-md-1 mb-0'),
                Column('dias_diferencia', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class FiltroMovBancario(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    tipo = forms.CharField(required=False)
    items = forms.IntegerField(max_value=30,
                               min_value=5,
                               required=False,
                               label='ítems x pág.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tipo_mov = (('', 'Todos'),) + TIPO_MOV_BANCARIO
        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.disable_csrf = True
        self.fields['tipo'].widget = SelectLiveSearchInput(choices=tipo_mov)
        self.fields['items'].widget = SelectLiveSearchInput(choices=ITEMS_X_PAG)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'

        self.helper.layout = Layout(
            Row(
                Column('buscar', css_class='form-group col-md-2 mb-0 '),
                Column('tipo', css_class='form-group col-md-2 mb-0 '),
                FieldWithButtons('items', boton_buscar(), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            )
        )


class MovBancarioForm(forms.ModelForm):
    class Meta:
        model = MovBancario
        fields = '__all__'
        labels = {
            "numero": "Número",
            "cotizacion": "Cotización",
            "observacion": "Observación",
            "nro_conciliacion": "Numero de conciliación",
        }

    emision = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False, label="Emisión")
    vencimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    acreditacion = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False, label="Acreditación")

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
                Column('emision', css_class='form-group col-md-2 mb-0'),
                Column('vencimiento', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('acreditacion', css_class='form-group col-md-2 mb-0'),
                Column('clearing', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('importe', css_class='form-group col-md-2 mb-0'),
                Column('cotizacion', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('concepto_bancario', css_class='form-group col-md-3 mb-0'),
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
                Submit('submit', 'Grabar movimiento', css_id='movSubmit', form="mov_form"),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class MovBancarios_DetalleForm(forms.ModelForm):
    class Meta:
        model = MovBancarios_Detalle
        fields = '__all__'
        labels = {
            "medio_pago": "Medio de pago",
            "importe_det": "Importe",
        }

    vencimiento_det = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False, label="Vencimiento")

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'detalles_form'
        self.fields['vencimiento_det'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.helper.layout = Layout(
            Row(
                Column('medio_pago', css_class='form-group col-md-1 mb-0'),
                Column('cheque', css_class='form-group col-md-1 mb-0'),
                Column('importe_det', css_class='form-group col-md-1 mb-0'),
                Column('vencimiento_det', css_class='form-group col-md-1 mb-0'),
                Column('cheque_numero', css_class='form-group col-md-1 mb-0'),
                Column('estado_anterior', css_class='form-group col-md-1 mb-0'),
                Submit('submit', 'Grabar detalle', css_id="detallesSubmit", form="detalles_form"),
                Column('det_id', type='hidden', css_class='form-group col-md-1 mb-0', id='det_id'),
                css_class='form-row'
            ),
        )

        
class Cheques_TercerosForm(forms.ModelForm):
    class Meta:
        model = Cheques_Terceros
        fields = '__all__'

    vencimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    acreditacion = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False, label="Acreditación")
    ingreso = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    egreso = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)

    def __init__(self, *args, **kwargs):
        
        initial = kwargs.get('initial', {})
        try:
            id = kwargs.pop('id')
        except Exception as e:
            pass
        try:
            initial['vencimiento'] = Cheques_Terceros.objects.get(pk=id).vencimiento.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['acreditacion'] = Cheques_Terceros.objects.get(pk=id).acreditacion.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['ingreso'] = Cheques_Terceros.objects.get(pk=id).ingreso.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['egreso'] = Cheques_Terceros.objects.get(pk=id).egreso.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

        self.fields['vencimiento'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['acreditacion'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['ingreso'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['egreso'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.form_id = 'form'
        self.helper.layout = Layout(
            Row(
                Column('numero', css_class='form-group col-md-2 mb-0'),
                Column('endosado', css_class='form-group col-md-1 mb-0'),
                Column('a_la_orden', css_class='form-group col-md-1 mb-0'),
                Column('electronico', css_class='form-group col-md-1 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('banco', css_class='form-group col-md-3 mb-0'),
                Column('sucursal', css_class='form-group col-md-1 mb-0'),
                Column('cuenta_nro', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('localidad', css_class='form-group col-md-3 mb-0'),
                Column('importe', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('librador', css_class='form-group col-md-3 mb-0'),
                Column('librador_cuit', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('ingreso', css_class='form-group col-md-2 mb-0'),
                Column('vencimiento', css_class='form-group col-md-2 mb-0'),
                Column('clearing', css_class='form-group col-md-1 mb-0'),
                Column('acreditacion', css_class='form-group col-md-2 mb-0'),

                Column('egreso', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('asociado_ingreso', css_class='form-group col-md-3 mb-0'),
                Column('asociado_egreso', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('caja', css_class='form-group col-md-1 mb-0'),
                Column('estado', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('imputado_difcot', css_class='form-group col-md-2 mb-0'),
                Column('marcha_rechazado', css_class='form-group col-md-2 mb-0'),
                Column('debcre', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('observacion', css_class='form-group col-md-6 mb-0'),
            ),
            ButtonHolder(
                Submit('submit', 'Grabar', css_id='Submit'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class Cheques_PropiosForm(forms.ModelForm):
    class Meta:
        model = Cheques_Propios
        fields = '__all__'

    vencimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)
    acreditacion = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False,
                                   label="Acreditación")
    emision = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput(), required=False)

    def __init__(self, *args, **kwargs):

        initial = kwargs.get('initial', {})
        try:
            id = kwargs.pop('id')
        except Exception as e:
            pass
        try:
            initial['vencimiento'] = Cheques_Propios.objects.get(pk=id).vencimiento.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['acreditacion'] = Cheques_Propios.objects.get(pk=id).acreditacion.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        try:
            initial['emision'] = Cheques_Propios.objects.get(pk=id).emision.strftime('%d/%m/%Y')
        except Exception as e:
            pass
        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

        self.fields['vencimiento'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['acreditacion'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['emision'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.form_id = 'form'
        self.helper.layout = Layout(
            Row(
                Column('chequera', css_class='form-group col-md-2 mb-0'),
                Column('numero', css_class='form-group col-md-2 mb-0'),
                Column('importe', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('emision', css_class='form-group col-md-2 mb-0'),
                Column('vencimiento', css_class='form-group col-md-2 mb-0'),
                Column('acreditacion', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('observacion', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('entregado_a', css_class='form-group col-md-3 mb-0'),
                Column('estado', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('depositado', css_class='form-group col-md-3 mb-0'),
                Column('asociado_id', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('caja_nro', css_class='form-group col-md-3 mb-0'),
                Column('caja_tipo', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('nro_conciliacion', css_class='form-group col-md-3 mb-0'),
                Column('lote', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar', css_id='Submit'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )