from django.urls import path
from administracion.views import viajante_listar, viajante_editar, viajante_agregar, viajante_eliminar
from administracion.views import transporte_listar, transporte_editar, transporte_agregar, transporte_eliminar
from administracion.views import condiciondepago_listar, condiciondepago_editar, condiciondepago_agregar, condiciondepago_eliminar
from administracion.views import deposito_listar, deposito_editar, deposito_agregar, deposito_eliminar
from administracion.views import mediodepago_listar, mediodepago_editar, mediodepago_agregar, mediodepago_eliminar
from administracion.views import grupocontactos_listar, grupocontactos_editar, grupocontactos_agregar, grupocontactos_eliminar
from administracion.views import grupoeconomico_listar, grupoeconomico_editar, grupoeconomico_agregar, grupoeconomico_eliminar
from administracion.views import moneda_listar, moneda_editar, moneda_agregar, moneda_eliminar
from .views import departamento_listar, departamento_agregar, departamento_editar, departamento_eliminar, \
    deposito_eliminar, deposito_editar, deposito_agregar, deposito_listar

urlpatterns = [
    path('departamento_listar/', departamento_listar, name='departamento_listar'),
    path('departamento_agregar/', departamento_agregar, name='departamento_agregar'),
    path('departamento_editar/<int:id>/', departamento_editar, name='departamento_editar'),
    path('departamento_eliminar/<int:id>/', departamento_eliminar, name='departamento_eliminar'),

    path('deposito_listar/', deposito_listar, name='deposito_listar'),
    path('deposito_agregar/', deposito_agregar, name='deposito_agregar'),
    path('deposito_editar/<int:id>/', deposito_editar, name='deposito_editar'),
    path('deposito_eliminar/<int:id>/', deposito_eliminar, name='deposito_eliminar'),

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

    path('deposito_listar/', deposito_listar, name='deposito_listar'),
    path('deposito_editar/<int:id>', deposito_editar, name='deposito_editar'),
    path('deposito_agregar/', deposito_agregar, name='deposito_agregar'),
    path('deposito_eliminar/<int:id>', deposito_eliminar, name='deposito_eliminar'),

    path('mediodepago_listar/', mediodepago_listar, name='mediodepago_listar'),
    path('mediodepago_editar/<int:id>', mediodepago_editar, name='mediodepago_editar'),
    path('mediodepago_agregar/', mediodepago_agregar, name='mediodepago_agregar'),
    path('mediodepago_eliminar/<int:id>', mediodepago_eliminar, name='mediodepago_eliminar'),

    path('moneda_listar/', moneda_listar, name='moneda_listar'),
    path('moneda_editar/<int:id>', moneda_editar, name='moneda_editar'),
    path('moneda_agregar/', moneda_agregar, name='moneda_agregar'),
    path('moneda_eliminar/<int:id>', moneda_eliminar, name='moneda_eliminar'),


    path('grupocontactos_listar/', grupocontactos_listar, name='grupocontactos_listar'),
    path('grupocontactos_editar/<int:id>', grupocontactos_editar, name='grupocontactos_editar'),
    path('grupocontactos_agregar/', grupocontactos_agregar, name='grupocontactos_agregar'),
    path('grupocontactos_eliminar/<int:id>', grupocontactos_eliminar, name='grupocontactos_eliminar'),


    path('grupoeconomico_listar/', grupoeconomico_listar, name='grupoeconomico_listar'),
    path('grupoeconomico_editar/<int:id>', grupoeconomico_editar, name='grupoeconomico_editar'),
    path('grupoeconomico_agregar/', grupoeconomico_agregar, name='grupoeconomico_agregar'),
    path('grupoeconomico_eliminar/<int:id>', grupoeconomico_eliminar, name='grupoeconomico_eliminar'),
]



