from administracion.forms import FiltroDepartamentos
from .models import Departamento
from tabla.filters import paginador
from tabla.forms import FiltroSimple
from django.db.models import Q


def administracion_filtrar(query_dict):
    codigo = query_dict.GET.get('codigo')
    descripcion = query_dict.GET.get('descripcion')
    listas_precios = query_dict.GET.get('listas_precios')
    utilidad_x_defecto = query_dict.GET.get('utilidad_x_defecto')
    rubro = query_dict.GET.get('rubro')
    actualiza_costos = query_dict.GET.get('actualiza_costos')
    imagen = query_dict.GET.get('imagen')

    buscar = query_dict.GET.get('buscar')
    filtrado = Departamento.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(codigo__icontains=buscar) |
                                   Q(descripcion__icontains=buscar) |
                                   Q(rubro__codigo__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroDepartamentos(initial={'codigo': codigo,
                                        'descripcion': descripcion,
                                        'listas_precios': listas_precios,
                                        'utilidad_x_defecto': utilidad_x_defecto,
                                        'rubro': rubro,
                                        'actualiza_costos': actualiza_costos,
                                        'imagen': imagen,
                                        })
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}
