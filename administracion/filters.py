from administracion.forms import FiltroDepartamentos, FiltroDepositos
from .models import Departamento, Deposito
from tabla.filters import paginador
from django.db.models import Q


def departamento_filtrar(query_dict):
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


def deposito_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = Deposito.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroDepositos(initial={'buscar': buscar,
                                    'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}
