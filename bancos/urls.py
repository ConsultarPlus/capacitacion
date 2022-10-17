from django.urls import path

from bancos.views import cuenta_bancaria_eliminar, chequera_eliminar, chequera_editar, chequera_agregar, \
    chequera_listar, cuenta_bancaria_editar, cuenta_bancaria_agregar, cuenta_bancaria_listar, mov_bancario_eliminar, \
    mov_bancario_editar, mov_bancario_agregar, mov_bancario_listar

urlpatterns = [
    path('cuenta_bancaria_listar/', cuenta_bancaria_listar, name='cuenta_bancaria_listar'),
    path('cuenta_bancaria_agregar/', cuenta_bancaria_agregar, name='cuenta_bancaria_agregar'),
    path('cuenta_bancaria_editar/<int:id>/', cuenta_bancaria_editar, name='cuenta_bancaria_editar'),
    path('cuenta_bancaria_eliminar/<int:id>/', cuenta_bancaria_eliminar, name='cuenta_bancaria_eliminar'),

    path('chequera_listar/', chequera_listar, name='chequera_listar'),
    path('chequera_agregar/', chequera_agregar, name='chequera_agregar'),
    path('chequera_editar/<int:id>/', chequera_editar, name='chequera_editar'),
    path('chequera_eliminar/<int:id>/', chequera_eliminar, name='chequera_eliminar'),

    path('mov_bancario_listar/', mov_bancario_listar, name='mov_bancario_listar'),
    path('mov_bancario_agregar/', mov_bancario_agregar, name='mov_bancario_agregar'),
    path('mov_bancario_editar/<int:id>/', mov_bancario_editar, name='mov_bancario_editar'),
    path('mov_bancario_eliminar/<int:id>/', mov_bancario_eliminar, name='mov_bancario_eliminar'),
]