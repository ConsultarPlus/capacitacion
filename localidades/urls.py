from django.urls import path

from localidades.views import pais_listar, pais_agregar, pais_editar, pais_eliminar, provincia_eliminar, \
    provincia_editar, provincia_agregar, provincia_listar, localidad_eliminar, localidad_editar, localidad_agregar, \
    localidad_listar, cargar_provincias, cargar_localidades

urlpatterns = [
    path('pais_listar/', pais_listar, name='pais_listar'),
    path('pais_agregar/', pais_agregar, name='pais_agregar'),
    path('pais_editar/<int:id>/', pais_editar, name='pais_editar'),
    path('pais_eliminar/<int:id>/', pais_eliminar, name='pais_eliminar'),

    path('provincia_listar/', provincia_listar, name='provincia_listar'),
    path('provincia_agregar/', provincia_agregar, name='provincia_agregar'),
    path('provincia_editar/<int:id>/', provincia_editar, name='provincia_editar'),
    path('provincia_eliminar/<int:id>/', provincia_eliminar, name='provincia_eliminar'),

    path('localidad_listar/', localidad_listar, name='localidad_listar'),
    path('localidad_agregar/', localidad_agregar, name='localidad_agregar'),
    path('localidad_editar/<int:id>/', localidad_editar, name='localidad_editar'),
    path('localidad_eliminar/<int:id>/', localidad_eliminar, name='localidad_eliminar'),

    path('cargar_provincias/', cargar_provincias, name='ajax_cargar_provincias'),
    path('cargar_localidades/', cargar_localidades, name='ajax_cargar_localidades')
    ]