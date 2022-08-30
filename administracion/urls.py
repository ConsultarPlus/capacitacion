from django.urls import path
from administracion.views import viajante_listar, viajante_editar, viajante_agregar, viajante_eliminar
from administracion.views import transporte_listar, transporte_editar, transporte_agregar, transporte_eliminar
from administracion.views import condiciondepago_listar, condiciondepago_editar, condiciondepago_agregar, condiciondepago_eliminar


urlpatterns = [
    path('viajante_listar/', viajante_listar, name='viajante_listar'),
    path('viajante_editar/<int:id>', viajante_editar, name='viajante_editar'),
    path('viajante_agregar/', viajante_agregar, name='viajante_agregar'),
    path('viajante_eliminar/<int:id>', viajante_eliminar, name='viajante_eliminar'),

    path('transporte_listar/', transporte_listar, name='transporte_listar'),
    path('transporte_editar/<int:id>', transporte_editar, name='transporte_editar'),
    path('transporte_agregar/', transporte_agregar, name='transporte_agregar'),
    path('transporte_eliminar/<int:id>', transporte_eliminar, name='transporte_eliminar'),

    path('condiciondepago_listar/', condiciondepago_listar, name='condiciondepago_listar'),
    path('condiciondepago_editar/<int:id>', condiciondepago_editar, name='condiciondepago_editar'),
    path('condiciondepago_agregar/', condiciondepago_agregar, name='condiciondepago_agregar'),
    path('condiciondepago_eliminar/<int:id>', condiciondepago_eliminar, name='condiciondepago_eliminar'),
]

