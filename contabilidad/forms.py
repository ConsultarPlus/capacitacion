from django import forms
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, ButtonHolder, Layout, Row, Column, Button
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG, SINO
from tabla.widgets import SelectLiveSearchInput
from contabilidad.models import PlanDeCuentas, Ejercicio, Asientos, AsientosDetalle
from tabla.widgets import DatePickerInput
import datetime
from .models import ENTIDAD
from tabla.gets import get_choices_mas_vacio


class FiltroPlanDeCuentas(forms.Form):
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


class PlanDeCuentasForm(forms.ModelForm):

    class Meta:
        model = PlanDeCuentas
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        V1 = int(kwargs.pop('V1', 1))
        V2 = int(kwargs.pop('V2', 1))
        V3 = int(kwargs.pop('V3', 2))
        V4 = int(kwargs.pop('V4', 2))
        V5 = int(kwargs.pop('V5', 2))

        super().__init__(*args, **kwargs)

        if V1:
            self.fields['cuenta_contable'].help_text = f"{'0'*V1}.{'0'*V2}.{'0'*V3}.{'0'*V4}.{'0'*V5}"

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('cuenta_contable', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('desglosable', css_class='form-group col-md-3 mb-0'),
                Column('monetaria', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('observacion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                HTML("""<br>"""),
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = '__all__'

    ejercicio = forms.CharField(required=True)
    descripcion = forms.CharField(required=False)
    fecha_desde = forms.DateField(input_formats=['%d/%m/%y'], widget=DatePickerInput(), required=False,
                            initial=datetime.date.today().strftime('%d/%m/%y'))
    fecha_hasta = forms.DateField(input_formats=['%d/%m/%y'], widget=DatePickerInput(), required=False,
                            initial=datetime.date.today().strftime('%d/%m/%y'))

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.helper = FormHelper()
        self.fields['ejercicio'].label = 'Ejercicio'
        self.fields['descripcion'].label = 'Descripción'
        self.fields['fecha_desde'].label = 'Fecha Desde'
        self.fields['fecha_hasta'].label = 'Fecha Hasta'
        self.helper.layout = Layout(
            Row(
                Column('ejercicio', css_class='form-group col-md-3 mb-0 '),
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-3 mb-0 ')
            ),
            Row(
                Column('fecha_desde', css_class='form-group col-md-2 mb-0 ')
            ),
            Row(
                Column('fecha_hasta', css_class='form-group col-md-2 mb-0 ')
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class AsientosForm(forms.ModelForm):
    class Meta:
        model = Asientos
        fields = '__all__'

    fecha = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput())
    fecha_movimiento = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput())
    fecha_creacion = forms.DateField(input_formats=['%d/%m/%Y'], widget=DatePickerInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero'].label = 'Numero'
        self.fields['orden'].label = 'Orden'
        self.fields['fecha'].label = 'Fecha'
        self.fields['observacion'].label = 'Observación'
        self.fields['observacion'].widget.attrs['rows'] = 6
        self.fields['fecha_movimiento'].label = 'Fecha De Movimiento'
        self.fields['asociado_id'].label = 'Asociado Id'
        self.fields['asociado_entidad'].widget = forms.Select(choices=ENTIDAD)
        self.fields['provisorio'].widget = forms.Select(choices=SINO)
        self.fields['manual'].widget = forms.Select(choices=SINO)
        self.fields['redondeo_haber'].label = 'Redondeo Haber'
        self.fields['redondeo_debe'].label = 'Redondeo Debe'
        self.fields['usuario'].label = 'Usuario'
        self.fields['fecha_creacion'].label = 'Fecha Creación'
        self.fields['lote'].label = 'Lote'
        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('numero', css_class='form-group col-md-2 mb-0'),
                Column('orden', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('observacion', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('fecha', css_class='form-group col-md-2 mb-0'),
                Column('fecha_movimiento', css_class='form-group col-md-2 mb-0'),
                Column('fecha_creacion', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('asociado_id', css_class='form-group col-md-2 mb-0'),
                Column('asociado_entidad', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('provisorio', css_class='form-group col-md-2 mb-0'),
                Column('manual', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('patente', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('redondeo_haber', css_class='form-group col-md-3 mb-0'),
                Column('redondeo_debe', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('usuario', css_class='form-group col-md-2 mb-0'),
                Column('observaciones', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('lote', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
          )


class AsientosDetalleForm(forms.ModelForm):
    class Meta:
        model = AsientosDetalle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asientos'].label = 'Asientos'
        self.fields['orden'].label = 'Orden'
        self.fields['fecha'].label = 'Fecha'
        self.fields['plan_de_cuentas'].label = 'Plan De Cuentas'
        self.fields['concepto'].widget = SelectLiveSearchInput(choices=get_choices_mas_vacio('CONCEPTO_CONTABLE'))
        self.fields['debe'].label = 'Debe'
        self.fields['haber'].label = 'Haber'
        self.fields['concepto_costo'].label = 'Concepto Costo'
        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('asientos', css_class='form-group col-md-2 mb-0'),
                Column('orden', css_class='form-group col-md-2 mb-0'),
                Column('fecha', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('plan_de_cuentas', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('concepto', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('debe', css_class='form-group col-md-3 mb-0'),
                Column('haber', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('concepto_costo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
          )
