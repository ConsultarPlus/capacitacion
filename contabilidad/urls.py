from django.urls import path
from tabla.views import variable_editar
from contabilidad.views import plan_de_cuentas_listar,\
                            plan_de_cuentas_eliminar,\
                            plan_de_cuentas_editar, \
                            plan_de_cuentas_agregar

urlpatterns = [
    path('plan_de_cuentas_listar/', plan_de_cuentas_listar, name='plan_de_cuentas_listar'),
    path('plan_de_cuentas_agregar/', plan_de_cuentas_agregar, name='plan_de_cuentas_agregar'),
    path('plan_de_cuentas_editar/<int:id>/', plan_de_cuentas_editar, name='plan_de_cuentas_editar'),
    path('plan_de_cuentas_eliminar/<int:id>/', plan_de_cuentas_eliminar, name='plan_de_cuentas_eliminar'),
    path('variable_editar/<slug:variable_id>/', variable_editar, name='variable_editar')
    ]