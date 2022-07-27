from perfiles.funcs import get_preferencia, get_variable
from django.template.defaulttags import register
from datetime import datetime


@register.simple_tag(takes_context=True)
def preferencia(context, vista, opcion, tipo_dato='L', default=False):
    usuario = context['user']
    return get_preferencia(usuario, vista, opcion, tipo_dato, default)


@register.simple_tag
def ano_en_rango(fecha):
    rango = get_variable('V_RANGO_AÑOS' '18;100')
    rango = rango.split(';')
    try:
        min = int(rango[0])
    except Exception as e:
        min = 18
    try:
        max = int(rango[1])
    except Exception as e:
        max = 100

    if min > max:
        aux = min
        min = max
        max = aux

    mensaje = ''

    if fecha > 0:
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        if ((datetime.today() - fecha).days/365) < min:
            mensaje = 'Menor de {} años'.format(min)
        elif ((datetime.today() - fecha).days/365) > max:
            mensaje = 'Mayor de {} años'.format(max)

    return mensaje
