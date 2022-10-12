from django.db.models import Q

from finanzas.forms import FiltroCaja, FiltroCajaCierres
from finanzas.models import Caja, CajaCierres, CierresMedio
from tabla.filters import paginador


def caja_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = Caja.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroCaja(initial={'buscar': buscar,
                               'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def caja_cierres_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado_cierres = CajaCierres.objects.all()
    filtrado_medios = CierresMedio.objects.all()

    if buscar != '' and buscar is not None:
        filtrado_cierres = filtrado_cierres.filter(Q(numero__icontains=buscar) |
                                                   Q(caja__descripcion__icontains=buscar)
                                                   )
        filtrado_medios = filtrado_medios.filter(Q(caja_cierre__in=filtrado_cierres))

    registros = filtrado_cierres.count()
    filtrado_cierres = filtrado_cierres.order_by('-numero')
    paginado_cierres = paginador(query_dict, filtrado_cierres)
    paginado_medios = paginador(query_dict, filtrado_medios)

    form = FiltroCajaCierres(initial={'buscar': buscar,
                                      'items': items})
    return {'filter': filtrado_cierres,
            'filter_m': filtrado_medios,
            'paginado': paginado_cierres,
            'paginado_m': paginado_medios,
            'registros': registros,
            'filtros_form': form}