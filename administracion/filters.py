from django.db.models import Q
from django.db.models import Sum
from administracion.models import Viajante, Transporte, CondicionDePago, Deposito, MedioDePago, Moneda
from tabla.funcs import es_valido
from perfiles.funcs import get_opcion_paginado
from tabla.forms import FiltroSimple, FiltroSimpleMasActivos
from administracion.forms import FiltroDepartamentos, FiltroDepositos
from .models import Departamento, Deposito
from tabla.filters import paginador


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
    filtrado = CondicionDePago.objects.all().order_by('id')

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
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def deposito_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    filtrado = Deposito.objects.all()
    activos = query_dict.GET.get('activos')

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
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
            'deposito': paginado,
            'registros': registros,
            'filtros_form': form}


def mediodepago_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    filtrado = MedioDePago.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
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


def moneda_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    filtrado = Moneda.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
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