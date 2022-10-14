from django.urls import path, include
from .views import menu, pagina_anterior


urlpatterns = [
    path('', menu, name='menu'),
    path('administracion/', include('administracion.urls')),
    path('localidades/', include('localidades.urls')),
    path('contabilidad/', include('contabilidad.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('bancos/', include('bancos.urls')),
    path('numeradores/', include('numeradores.urls')),
    path('tabla/', include('tabla.urls')),
    path('mensajes/', include('mensajes.urls')),
    path('documentos/', include('documentos.urls')),
    path('perfiles/', include('perfiles.urls')),
    path('pagina_anterior/', pagina_anterior, name='pagina_anterior'),
]
