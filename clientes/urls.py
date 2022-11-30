from django.urls import path
from .views import (cliente_agregar,
                    clientes_listar,
                    cliente_editar,
                    cliente_eliminar,
                    clientes_cargar_csv,
                    cliente_agregar_y_volver,
                    tipos_iva_eliminar,
                    tipos_iva_editar,
                    tipos_iva_listar,
                    tipos_iva_agregar)

urlpatterns = [
    path('cliente_agregar/', cliente_agregar, name='cliente_agregar'),
    path('cliente_agregar_y_volver/', cliente_agregar_y_volver, name='cliente_agregar_y_volver'),
    path('clientes_listar/', clientes_listar, name='clientes_listar'),
    path('cliente_editar/<slug:encriptado>/', cliente_editar, name='cliente_editar'),
    path('cliente_eliminar/<int:id>/', cliente_eliminar, name='cliente_eliminar'),
    path('cliente_importar/', clientes_cargar_csv, name='cliente_importar'),
    
    path('tipos_iva_agregar/', tipos_iva_agregar, name='tipos_iva_agregar'),
    path('tipos_iva_listar/', tipos_iva_listar, name='tipos_iva_listar'),
    path('tipos_iva_editar/<int:id>/', tipos_iva_editar, name='tipos_iva_editar'),
    path('tipos_iva_eliminar/<int:id>/', tipos_iva_eliminar, name='tipos_iva_eliminar'),
]
