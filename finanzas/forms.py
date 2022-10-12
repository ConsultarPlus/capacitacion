from django import forms
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Row, Column, Button
from finanzas.models import Caja, CajaCierres, CierresMedio
from tabla.funcs import boton_buscar
from tabla.listas import ITEMS_X_PAG
from tabla.widgets import SelectLiveSearchInput


class FiltroCaja(forms.Form):
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


class CajaForm(forms.ModelForm):

    class Meta:
        model = Caja
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('codigo', css_class='form-group col-md-3 mb-0'),
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                Column('cuenta_contable', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )
        
        
class FiltroCajaCierres(forms.Form):
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


class CajaCierresForm(forms.ModelForm):

    class Meta:
        model = CajaCierres
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('saldo_apertura_anterior', css_class='form-group col-md-4 mb-0'),
                Column('saldo_cierre_anterior', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('saldo_cheques', css_class='form-group col-md-4 mb-0'),
                Column('saldo_apertura', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )



class CierresMedioForm(forms.ModelForm):

    class Meta:
        model = CierresMedio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        cierre = kwargs.pop('cierre')

        super().__init__(*args, **kwargs)

        self.fields['caja_cierre'].initial = cierre
        self.helper = FormHelper()
        self.helper.form_id = 'id_form'
        self.helper.layout = Layout(
            Row(
                Column('medio_de_pago', css_class='form-group col-md-3 mb-0'),
                Column('cuenta_contable', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('descripcion', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Grabar'),
                Button('cancel', 'Volver', css_class='btn-default', onclick="window.history.back()")
            )
        )
