from django.urls import path
from administracion.views import viajante_listar, viajante_editar, viajante_agregar, viajante_eliminar


urlpatterns = [
    path('viajante_listar/', viajante_listar, name='viajante_listar'),
    path('viajante_editar/<int:id>', viajante_editar, name='viajante_editar'),
    path('viajante_agregar/', viajante_agregar, name='viajante_agregar'),
    path('viajante_eliminar/<int:id>', viajante_eliminar, name='viajante_eliminar'),
]