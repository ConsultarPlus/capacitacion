from django.urls import path
from finanzas.views import caja_cierres_eliminar, caja_cierres_agregar, caja_cierres_listar, caja_eliminar, \
    caja_editar, caja_agregar, caja_listar, cierres_medio_eliminar, cierres_medio_agregar, cierres_medio_listar

urlpatterns = [
    path('caja_listar/', caja_listar, name='caja_listar'),
    path('caja_agregar/', caja_agregar, name='caja_agregar'),
    path('caja_editar/<int:id>/', caja_editar, name='caja_editar'),
    path('caja_eliminar/<int:id>/', caja_eliminar, name='caja_eliminar'),

    path('caja_cierres_listar/', caja_cierres_listar, name='caja_cierres_listar'),
    path('caja_cierres_agregar/<int:id>/', caja_cierres_agregar, name='caja_cierres_agregar'),
    path('caja_cierres_eliminar/<int:id>/', caja_cierres_eliminar, name='caja_cierres_eliminar'),

    path('cierres_medio_listar/', cierres_medio_listar, name='cierres_medio_listar'),
    path('cierres_medio_agregar/<int:id>/', cierres_medio_agregar, name='cierres_medio_agregar'),
    path('cierres_medio_eliminar/<int:id>/', cierres_medio_eliminar, name='cierres_medio_eliminar'),
]