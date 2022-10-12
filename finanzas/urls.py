from django.urls import path
from finanzas.views import caja_cierres_agregar, caja_cierres_listar, caja_eliminar, \
    caja_editar, caja_agregar, caja_listar, cierres_medio_agregar

urlpatterns = [
    path('caja_listar/', caja_listar, name='caja_listar'),
    path('caja_agregar/', caja_agregar, name='caja_agregar'),
    path('caja_editar/<int:id>/', caja_editar, name='caja_editar'),
    path('caja_eliminar/<int:id>/', caja_eliminar, name='caja_eliminar'),

    path('caja_cierres_listar/', caja_cierres_listar, name='caja_cierres_listar'),
    path('caja_cierres_agregar/<int:id>/', caja_cierres_agregar, name='caja_cierres_agregar'),

    path('cierres_medio_agregar/<int:id>/', cierres_medio_agregar, name='cierres_medio_agregar'),
]