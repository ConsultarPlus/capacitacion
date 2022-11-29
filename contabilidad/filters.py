from django.contrib import messages
from django.db.models import Q
from tabla.filters import paginador
from tabla.forms import FiltroSimple
from contabilidad.forms import FiltroPlanDeCuentas, EjercicioForm, AsientosForm, AsientosDetalleForm
from contabilidad.models import PlanDeCuentas, Ejercicio, Asientos, AsientosDetalle
from tabla.gets import get_variable
from tabla.models import Variable
from perfiles.funcs import get_opcion_paginado



def plan_de_cuentas_filtrar(query_dict):
    items = query_dict.GET.get('items')
    buscar = query_dict.GET.get('buscar')

    filtrado = PlanDeCuentas.objects.all()

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(cuenta_contable__icontains=buscar) |
                                   Q(descripcion__icontains=buscar)
                                   )

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroPlanDeCuentas(initial={'buscar': buscar,
                                        'items': items,
                                        })
    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'filtros_form': form}


def cuenta_contable_valida2(request, form):  # esta funcion es un quilombo, seguro se puede mejorar
    cuenta_contable = str(form['cuenta_contable']).strip()  # dos variables con el valor cuenta_contable, una desechable
    cuenta_contable_disp = str(form['cuenta_contable']).strip()
    pos_total = -1
    pos = cuenta_contable.find(".")
    i = 0
    var_dict = {'V_N1': int(get_variable("V_N1", 1)),
                'V_N2': int(get_variable("V_N2", 1)),
                'V_N3': int(get_variable("V_N3", 2)),
                'V_N4': int(get_variable("V_N4", 2)),
                'V_N5': int(get_variable("V_N5", 2))}

    while pos != -1:
        pos = cuenta_contable_disp.find(".")  # actualizar la posicion
        pos_total += pos + 1
        cuenta_contable_disp = cuenta_contable_disp[pos + 1:]  # cortar la cuenta contable para el siguiente chequeo

        if var_dict[f'V_N{i+1}'] != pos and pos != -1 or pos == -1 and var_dict[f'V_N{i+1}'] != len(cuenta_contable_disp):  # verifica que la sintaxis sea correcta
            mensaje = 'La sintaxis de la cuenta contable no es correcta.'
            messages.add_message(request, messages.ERROR, mensaje)
            return False

        if not PlanDeCuentas.objects.filter(cuenta_contable=cuenta_contable[0:pos_total]).exists():  # verifica que la cuenta contable padre exista
            mensaje = 'La cuenta contable padre no existe'
            messages.add_message(request, messages.ERROR, mensaje)
            return False

        i += 1  # actualizar el contador
    return True


def ejercicio_filtrar(query_dict):
    ejercicio = query_dict.GET.get('ejercicio')
    descripcion = query_dict.GET.get('descripcion')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')

    filtrado = Ejercicio.objects.all()

    if ejercicio != '' and ejercicio is not None:
        filtrado = filtrado.filter(ejercicio=ejercicio)

    if descripcion != '' and descripcion is not None:
        filtrado = filtrado.filter(descripcion=descripcion)

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroSimple(initial={'items': items,
                                 'modo': modo})

    return {'filter': filtrado,
            'ejercicio': paginado,
            'registros': registros,
            'filtros_form': form}


def asientos_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')
    asociado_id = query_dict.GET.get('asociado_id')
    orden = query_dict.GET.get('orden')
    numero = query_dict.GET.get('numero')

    filtrado = Asientos.objects.all().order_by('asociado_id', 'numero', 'orden')

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(Q(asociado_id=asociado_id) |
                                  (Q(numero=numero) |
                                   Q(orden=orden)
                                   ))

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroSimple(initial={'items': items,
                                 'asociado_id': asociado_id,
                                 'numero': numero,
                                 'orden': orden,
                                 'modo': modo})

    return {'filter': filtrado,
            'paginado': paginado,
            'registros': registros,
            'asociado_id': asociado_id,
            'numero': numero,
            'orden': orden,
            'filtros_form': form}


def asientos_detalle_filtrar(query_dict):
    buscar = query_dict.GET.get('buscar')
    items = get_opcion_paginado(query_dict)
    modo = query_dict.GET.get('modo')

    filtrado = AsientosDetalle.objects.all().order_by('asientos_detalle')

    if buscar != '' and buscar is not None:
        filtrado = filtrado.filter(buscar=buscar)

    registros = filtrado.count()
    paginado = paginador(query_dict, filtrado)

    form = FiltroSimple(initial={'items': items,
                                 'modo': modo})

    return {'filter': filtrado,
            'asientosdetalle': paginado,
            'registros': registros,
            'filtros_form': form}
