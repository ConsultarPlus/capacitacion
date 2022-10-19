from crispy_forms.bootstrap import FieldWithButtons
from localidades.models import Pais, Provincia, Localidad
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG
from tabla.widgets import SelectLiveSearchInput
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML


class FiltroPais(forms.Form):
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


class PaisForm(forms.ModelForm):

    class Meta:
        model = Pais
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('codigo', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                Column('siap', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )


class FiltroProvincia(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
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

        try:
            seleccionar_pais = kwargs['initial']['pais']
            if seleccionar_pais is not None and seleccionar_pais != '':
                self.fields['pais'].initial = seleccionar_pais
        except (ValueError, TypeError):
            pass

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'

        self.helper.layout = Layout(
            Row(
                Column('buscar', css_class='form-group col-md-2 mb-0 '),
                Column('pais', css_class='form-group col-md-2 mb-0 '),
                FieldWithButtons('items', boton_buscar(), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ))


class ProvinciaForm(forms.ModelForm):

    class Meta:
        model = Provincia
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
                Column('pais', css_class='form-group col-md-3 mb-0'),
                Column('cuenta_contable', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('inscripto_ib', css_class='form-group col-md-3 mb-0'),
                Column('vencimiento_inscripcion', css_class='form-group col-md-3 mb-0'),
                Column('alicuota', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )
        
        
class FiltroLocalidad(forms.Form):
    buscar = forms.CharField(max_length=60, required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all(), required=False)
    items = forms.IntegerField(max_value=30,
                               min_value=5,
                               required=False,
                               label='Ítems x pág.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'GET'
        self.helper.disable_csrf = True
        self.helper.form_id = 'id_filtro_localidad'
        self.fields['items'].widget = SelectLiveSearchInput(choices=ITEMS_X_PAG)

        try:
            seleccionar_provincia = kwargs['initial']['provincia']
            if seleccionar_provincia is not None and seleccionar_provincia != '':
                self.fields['provincia'].initial = seleccionar_provincia
        except (ValueError, TypeError):
            pass

        try:
            seleccionar_pais = kwargs['initial']['pais']
            if seleccionar_pais is not None and seleccionar_pais != '':
                self.fields['pais'].initial = seleccionar_pais
        except (ValueError, TypeError):
            pass

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm'

        self.helper.layout = Layout(
            Row(
                Column('buscar', css_class='form-group col-md-2 mb-0 '),
                Column('pais', css_class='form-group col-md-2 mb-0 '),
                Column('provincia', css_class='form-group col-md-2 mb-0 '),
                FieldWithButtons('items', boton_buscar(), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ))


class LocalidadForm(forms.ModelForm):

    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)

    class Meta:
        model = Localidad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('codigo_postal', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-4 mb-0'),
                Column('caracteristica_telefonica', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('pais', css_class='form-group col-md-3 mb-0'),
                Column('provincia', css_class='form-group col-md-3 mb-0')
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )
