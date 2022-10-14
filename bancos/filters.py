from django.db.models import Q

from bancos.forms import FiltroCuentaBancaria, FiltroChequera
from bancos.models import CuentaBancaria, Chequera
from tabla.filters import paginador


def cuenta_bancaria_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = CuentaBancaria.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(cuenta__icontains=buscar) |
                                   Q(descripcion__icontains=buscar) |
                                   Q(banco__icontains=buscar) |
                                   Q(titular__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroCuentaBancaria(initial={'buscar': buscar,
                                         'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def chequera_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = Chequera.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroChequera(initial={'buscar': buscar,
                                   'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}

