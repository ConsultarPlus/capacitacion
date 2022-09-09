from localidades.forms import FiltroPais, FiltroProvincia, FiltroLocalidad
from localidades.models import Pais, Provincia, Localidad
from tabla.filters import paginador
from django.db.models import Q


def pais_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = query_dict.GET.get('items')

    filtrado = Pais.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroPais(initial={'buscar': buscar,
                               'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def provincia_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    pais = query_dict.GET.get('pais')
    items = query_dict.GET.get('items')

    filtrado = Provincia.objects.all()

    if pais != '' and pais is not None:
        filtrado = filtrado.filter(pais=pais)

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroProvincia(initial={'pais': pais,
                                    'buscar': buscar,
                                    'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def localidad_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    provincia = query_dict.GET.get('provincia')
    items = query_dict.GET.get('items')

    filtrado = Localidad.objects.all()

    if provincia != '' and provincia is not None:
        filtrado = filtrado.filter(provincia=provincia)

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo_postal__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroLocalidad(initial={'provincia': provincia,
                                    'buscar': buscar,
                                    'items': items})
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}
