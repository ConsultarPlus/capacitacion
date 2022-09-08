from django.urls import path
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
    path('deposito_eliminar/<int:id>/', deposito_eliminar, name='deposito_eliminar')
]