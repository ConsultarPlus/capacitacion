from administracion.forms import FiltroDepartamentos
from .models import Departamento
from tabla.filters import paginador
from tabla.models import Tabla
from django.db.models import Q


def administracion_filtrar(query_dict):
    # codigo = query_dict.GET.get('codigo')
    # descripcion = query_dict.GET.get('descripcion')
    # listas_precios = query_dict.GET.get('listas_precios')
    # utilidad_x_defecto = query_dict.GET.get('utilidad_x_defecto')
    # rubro = query_dict.GET.get('rubro')
    # actualiza_costos = query_dict.GET.get('actualiza_costos')
    # imagen = query_dict.GET.get('imagen')
    items = query_dict.GET.get('items')
    id_rubro = query_dict.GET.get('seleccionar_rubro')
    buscar = query_dict.GET.get('buscar')

    filtrado = Departamento.objects.all()

    if id_rubro != '' and id_rubro is not None:
        filtrado = filtrado.filter(rubro=id_rubro)

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroDepartamentos(initial={'seleccionar_rubro': id_rubro,
                                        'buscar': buscar,
                                        'items': items,
                                        })
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}
