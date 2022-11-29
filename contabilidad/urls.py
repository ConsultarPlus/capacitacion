from django.urls import path
from tabla.views import variable_editar
from contabilidad.views import plan_de_cuentas_listar,\
                            plan_de_cuentas_eliminar,\
                            plan_de_cuentas_editar, \
                            plan_de_cuentas_agregar, \
                            ejercicio_listar,\
                            ejercicio_eliminar,\
                            ejercicio_editar, \
                            ejercicio_agregar, \
                            asientos_listar,\
                            asientos_eliminar,\
                            asientos_editar, \
                            asientos_agregar, \
                            asientos_detalle_listar,\
                            asientos_detalle_eliminar,\
                            asientos_detalle_editar, \
                            asientos_detalle_agregar

urlpatterns = [
    path('plan_de_cuentas_listar/', plan_de_cuentas_listar, name='plan_de_cuentas_listar'),
    path('plan_de_cuentas_agregar/', plan_de_cuentas_agregar, name='plan_de_cuentas_agregar'),
    path('plan_de_cuentas_editar/<int:id>/', plan_de_cuentas_editar, name='plan_de_cuentas_editar'),
    path('plan_de_cuentas_eliminar/<int:id>/', plan_de_cuentas_eliminar, name='plan_de_cuentas_eliminar'),
    path('variable_editar/<slug:variable_id>/', variable_editar, name='variable_editar'),


    path('ejercicio_agregar/', ejercicio_agregar, name='ejercicio_agregar'),
    path('ejercicio_listar/', ejercicio_listar, name='ejercicio_listar'),
    path('ejercicio_editar/<int:id>/', ejercicio_editar, name='ejercicio_editar'),
    path('ejercicio_eliminar/<int:id>', ejercicio_eliminar, name='ejercicio_eliminar'),

    path('asientos_agregar/', asientos_agregar, name='asientos_agregar'),
    path('asientos_listar/', asientos_listar, name='asientos_listar'),
    path('asientos_editar/<int:id>/', asientos_editar, name='asientos_editar'),
    path('asientos_eliminar/<int:id>', asientos_eliminar, name='asientos_eliminar'),

    path('asientos_detalle_agregar/', asientos_detalle_agregar, name='asientos_detalle_agregar'),
    path('asientos_detalle_listar/', asientos_detalle_listar, name='asientos_detalle_listar'),
    path('asientos_detalle_editar/<int:id>/', asientos_detalle_editar, name='asientos_detalle_editar'),
    path('asientos_detalle_eliminar/<int:id>', asientos_detalle_eliminar, name='asientos_detalle_eliminar'),
]