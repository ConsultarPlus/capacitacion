from django.db.models import Q
from django.db.models import Sum
from administracion.models import Viajante, Transporte, CondicionDePago
from tabla.filters import paginador
from tabla.funcs import es_valido, normaliza_fechas
from perfiles.funcs import get_opcion_paginado, get_preferencia
from tabla.forms import FiltroSimple, FiltroSimpleMasActivos


def viajante_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    filtrado = Viajante.objects.all()
    activos = query_dict.GET.get('activos')

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(nombre__icontains=buscar)
                                   )
    if activos is None:
        activos = 'S'
    if es_valido(activos):
        if activos == 'S':
            filtrado = filtrado.filter(activo='S')

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroSimpleMasActivos(initial={'buscar': buscar,
                                           'activos': activos,
                                           'items': items,
                                           'modo': modo})
    return {'filter': filtrado,
            'viajante': paginado,
            'registros': registros,
            'filtros_form': form}


def transporte_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    filtrado = Transporte.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(nombre__icontains=buscar)
                                   )
    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroSimple(initial={'buscar': buscar,
                                 'items': items,
                                 'modo': modo})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def condiciondepago_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    filtrado = CondicionDePago.objects.all()
    activos = query_dict.GET.get('activos')

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(descripcion__icontains=buscar)
                                   )
    if activos is None:
        activos = 'S'
    if es_valido(activos):
        if activos == 'S':
            filtrado = filtrado.filter(activo='S')

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroSimpleMasActivos(initial={'buscar': buscar,
                                           'activos': activos,
                                           'items': items,
                                           'modo': modo})
    return {'filter': filtrado,
            'condiciondepago': paginado,
            'registros': registros,
            'filtros_form': form}