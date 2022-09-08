from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin


class DepartamentoAdmin(SimpleHistoryAdmin):
    list_display = ('codigo', 'descripcion', 'listas_precios', 'utilidad_x_defecto', 'rubro', 'actualiza_costos', 'imagen')
    search_fields = list_display


class DepositoAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'codigo', 'descripcion', 'afecta_stock', 'activo', 'domicilio', 'telefono')
    search_fields = list_display
