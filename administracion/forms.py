from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML
from crispy_forms.bootstrap import FieldWithButtons
from tabla.widgets import SelectLiveSearchInput
from tabla.funcs import boton_buscar
from tabla.listas import MODELOS, ITEMS_X_PAG, SINO, ACTIVO, PERIODO, CAJA, TIPO
from tabla.gets import get_choices_mas_vacio
from tabla.listas import ITEMS_X_PAG, ACTIVO, PERIODO
from administracion.models import Viajante, Transporte, CondicionDePago, MedioDePago, Moneda,Departamento, Deposito


class FiltroDepartamentos(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    seleccionar_rubro = forms.IntegerField(required=False)
    items = forms.IntegerField(max_value=30,
                               min_value=5,
                               required=False,
                               label='ítems x pág.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.disable_csrf = True
        self.fields['seleccionar_rubro'].widget = SelectLiveSearchInput(choices=get_choices_mas_vacio('RUBRO'))
        self.fields['items'].widget = SelectLiveSearchInput(choices=ITEMS_X_PAG)

        try:
            seleccionar_rubro = kwargs['initial']['seleccionar_rubro']
            if seleccionar_rubro is not None and seleccionar_rubro != '':
                self.fields['seleccionar_rubro'].initial = seleccionar_rubro
        except (ValueError, TypeError):
            pass

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'

        self.helper.layout = Layout(
            Row(
                Column('buscar', css_class='form-group col-md-2 mb-0 '),
                Column('seleccionar_rubro', css_class='form-group col-md-2 mb-0 '),
                FieldWithButtons('items', boton_buscar(), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ))


class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('codigo', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('utilidad_x_defecto', css_class='form-group col-md-3 mb-0'),
                Column('listas_precios', css_class='form-group col-md-3 mb-0'),
                Column('rubro', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('actualiza_costos', css_class='form-group col-md-5 mb-0'),
                Column('imagen', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class FiltroDepositos(forms.Form):
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
            ))


class DepositoForm(forms.ModelForm):

    class Meta:
        model = Deposito
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('codigo', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('afecta_stock', css_class='form-group col-md-3 mb-0'),
                Column('activo', css_class='form-group col-md-3 mb-0'),
                Column('externo', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('domicilio', css_class='form-group col-md-3 mb-0'),
                Column('telefono', css_class='form-group col-md-3 mb-0'),
                Column('localidad', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                HTML("""<br>"""),
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


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
        self.helper.layout = Layout(
            Row(
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
                Column('descripcion', css_class='form-group col-md-5 mb-0'),
                Column('activo', css_class='form-group col-md-2 mb-0'),

            ),
            Row(
                Column('cuotas', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('dia_vencimiento', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('periodo_cantidad', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('periodo', css_class='form-group col-md-3 mb-0'),

            ),
            Row(
                Column('porcentaje', css_class='form-group col-md-2 mb-0'),
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class DepositoForm(forms.ModelForm):

    class Meta:
        model = Deposito
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['codigo'].label = 'Código'
        self.fields['descripcion'].label = 'Descripción'
        self.fields['domicilio'].label = 'Domicilio'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['activo'].widget = SelectLiveSearchInput(choices=ACTIVO)
        self.fields['afecta_stock'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['externo'].widget = SelectLiveSearchInput(choices=SINO)
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(Row(
                Column('codigo', css_class='form-group col-md-3 mb-0'),
                Column('activo', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('domicilio', css_class='form-group col-md-3 mb-0'),
                Column('afecta_stock', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
            Column('telefono', css_class='form-group col-md-3 mb-0'),
            Column('externo', css_class='form-group col-md-2 mb-0'),
            css_class='form-row'
            ),
            Row(
                Column('localidad', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


def get_monedas():
    monedas = Moneda.objects.all().values('id','simbolo')
    choices = [(mon['id'], mon['simbolo']) for mon in monedas]
    choices.insert(0, ('', '-----'))
    return choices


class MedioDePagoForm(forms.ModelForm):
    class Meta:
        model = MedioDePago
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['codigo'].label = 'Código'
        self.fields['descripcion'].label = 'Descripción'
        self.fields['cuenta_contable'].label = 'Cuenta Contable'
        self.fields['cobro'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['pago'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['deposito'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['pide_moneda'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['pide_cuenta_bancaria'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['caja'].widget = SelectLiveSearchInput(choices=CAJA)
        self.fields['observacion'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['incluir_ff'].widget = SelectLiveSearchInput(choices=SINO)
        self.fields['moneda'].widget = SelectLiveSearchInput(choices=get_monedas())
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(Row(
                Column('codigo', css_class='form-group col-md-3 mb-0'),
                Column('cobro', css_class='form-group col-md-2 mb-0'),
                Column('pago', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('cuenta_contable', css_class='form-group col-md-3 mb-0'),
                Column('deposito', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pide_moneda', css_class='form-group col-md-2 mb-0'),
                Column('pide_cuenta_bancaria', css_class='form-group col-md-3 mb-0'),
                Column('caja', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('observacion', css_class='form-group col-md-3 mb-0'),
                Column('incluir_ff', css_class='form-group col-md-3 mb-0'),
                Column('moneda', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class MonedaForm(forms.ModelForm):

    class Meta:
        model = Moneda
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['descripcion'].label = 'Descripción'
        self.fields['simbolo'].label = 'Símbolo'
        self.fields['tipo'].widget = SelectLiveSearchInput(choices=TIPO)
        self.fields['siap'].label = 'Siap'

        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(Row(
                Column('descripcion', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('simbolo', css_class='form-group col-md-3 mb-0'),

            ),
            Row(
                Column('tipo', css_class='form-group col-md-3 mb-0'),

            ),
            Row(
                Column('siap', css_class='form-group col-md-3 mb-0'),

                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )