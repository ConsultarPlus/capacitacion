from django.contrib import messages
from django.db.models import Q
from tabla.filters import paginador
from contabilidad.forms import FiltroPlanDeCuentas
from contabilidad.models import PlanDeCuentas
from tabla.gets import get_variable
from tabla.models import Variable


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

        print("\n\n", cuenta_contable, pos_total, cuenta_contable_disp, pos, var_dict[f'V_N{i+1}'])

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

