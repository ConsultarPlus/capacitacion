from crispy_forms.bootstrap import FieldWithButtons
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG
from tabla.widgets import SelectLiveSearchInput
from .models import Departamento
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder


class FiltroDepartamentos(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    # rubro = forms.CharField(max_length=60, required=False)
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
                Column('listas_precios', css_class='form-group col-md-6 mb-0'),
                Column('utilidad_x_defecto', css_class='form-group col-md-6 mb-0'),
                Column('rubro', css_class='form-group col-md-6 mb-0'),
                Column('actualiza_costos', css_class='form-group col-md-6 mb-0'),
                Column('imagen', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )