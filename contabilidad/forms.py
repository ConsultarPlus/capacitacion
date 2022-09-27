from django import forms
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, ButtonHolder, Layout, Row, Column, Button
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG
from tabla.widgets import SelectLiveSearchInput
from contabilidad.models import PlanDeCuentas


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
