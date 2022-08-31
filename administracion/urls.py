from django.urls import path
from .views import departamento_listar, departamento_agregar, departamento_editar, departamento_eliminar

urlpatterns = [
    path('departamento_listar/', departamento_listar, name='departamento_listar'),
    path('departamento_agregar/', departamento_agregar, name='departamento_agregar'),
    path('departamento_editar/<int:id>/', departamento_editar, name='departamento_editar'),
    path('departamento_eliminar/<int:id>/', departamento_eliminar, name='departamento_eliminar')
]