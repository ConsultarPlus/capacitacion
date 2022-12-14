from django.db.models import Q

from bancos.forms import FiltroCuentaBancaria, FiltroChequera, FiltroMovBancario
from bancos.models import CuentaBancaria, Chequera, MovBancario, MovBancarios_Detalle, Cheques_Terceros, Cheques_Propios
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


def mov_bancario_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    tipo = query_dict.GET.get('tipo')
    items = query_dict.GET.get('items')

    filtrado = MovBancario.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(tipo__icontains=buscar) |
                                   Q(numero__icontains=buscar)
                                   )
    if tipo != '' and tipo is not None:
        filtrado = filtrado.filter(Q(tipo__icontains=tipo))

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroMovBancario(initial={'buscar': buscar,
                                      'tipo': tipo,
                                      'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def mov_bancarios_detalle_filtrar(query_dict):

    filtrado = MovBancarios_Detalle.objects.all()
    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros}


def cheques_terceros_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = Cheques_Terceros.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(numero__icontains=buscar) |
                                   Q(cuenta_nro__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroChequera(initial={'buscar': buscar,
                                   'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}

def cheques_propios_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = Cheques_Propios.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(numero__icontains=buscar) |
                                   Q(cuenta_nro__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroChequera(initial={'buscar': buscar,
                                   'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}
