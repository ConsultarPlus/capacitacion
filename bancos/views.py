from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt

from administracion.models import MedioDePago
from bancos.filters import cuenta_bancaria_filtrar, chequera_filtrar, mov_bancario_filtrar, \
    mov_bancarios_detalle_filtrar, cheques_terceros_filtrar
from bancos.forms import ChequeraForm, CuentaBancariaForm, MovBancarioForm, MovBancarios_DetalleForm, \
    Cheques_TercerosForm
from bancos.models import CuentaBancaria, Chequera, MovBancario, MovBancarios_Detalle, Cheques_Terceros
from perfiles.models import Perfil
from tabla.listas import TIPO_MOV_BANCARIO, DP_NE_CA_RE, DEBITO_CREDITO


@login_required(login_url='ingresar')
def cuenta_bancaria_listar(request):
    contexto = cuenta_bancaria_filtrar(request)
    template_name = 'cuenta_bancaria_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.cuenta_bancaria_agregar", None, raise_exception=True)
def cuenta_bancaria_agregar(request):
    if request.POST:
        form = CuentaBancariaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cuenta_bancaria_listar')
    else:
        form = CuentaBancariaForm()

    template_name = 'CuentaBancariaForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.cuenta_bancaria_editar", None, raise_exception=True)
def cuenta_bancaria_editar(request, id):
    try:
        cuenta_bancaria = CuentaBancaria.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('cuenta_bancaria_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = CuentaBancariaForm(post, request.FILES, instance=cuenta_bancaria, id=id)
        if form.is_valid():
            form.save()
            return redirect('cuenta_bancaria_listar')
    else:
        form = CuentaBancariaForm(instance=cuenta_bancaria, id=id)

    template_name = 'CuentaBancariaForm.html'
    contexto = {'form': form, 'CuentaBancaria': CuentaBancaria}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.cuenta_bancaria_eliminar", None, raise_exception=True)
def cuenta_bancaria_eliminar(request, id):
    url = 'cuenta_bancaria_listar'
    try:
        cuenta_bancaria = CuentaBancaria.objects.get(id=id)
        cuenta_bancaria.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


########################################################################################################################


@login_required(login_url='ingresar')
def chequera_listar(request):
    contexto = chequera_filtrar(request)
    template_name = 'chequera_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.chequera_agregar", None, raise_exception=True)
def chequera_agregar(request):
    if request.POST:
        form = ChequeraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chequera_listar')
    else:
        form = ChequeraForm()

    template_name = 'ChequeraForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.chequera_editar", None, raise_exception=True)
def chequera_editar(request, id):
    try:
        chequera = Chequera.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('chequera_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = ChequeraForm(post, request.FILES, instance=chequera, id=id)
        if form.is_valid():
            form.save()
            return redirect('chequera_listar')
    else:
        form = ChequeraForm(instance=chequera, id=id)

    template_name = 'ChequeraForm.html'
    contexto = {'form': form, 'Chequera': Chequera}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.chequera_eliminar", None, raise_exception=True)
def chequera_eliminar(request, id):
    url = 'chequera_listar'
    try:
        chequera = Chequera.objects.get(id=id)
        chequera.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


########################################################################################################################


@login_required(login_url='ingresar')
def mov_bancario_listar(request):
    contexto = mov_bancario_filtrar(request)
    template_name = 'mov_bancario_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.mov_bancario_agregar_dc", None, raise_exception=True)
def mov_bancario_agregar(request):
    choices = DP_NE_CA_RE
    usuario_actual = Perfil.objects.get(user=request.user.pk)
    if request.POST:
        movForm = MovBancarioForm(request.POST, request.FILES, user=usuario_actual, choices=choices)
        if request.POST['submit'] == "Grabar movimiento":
            nuevo_mov = movForm.save()
            return redirect('mov_bancario_editar', id=nuevo_mov.pk)
    else:
        movForm = MovBancarioForm(user=usuario_actual, choices=choices)

    template_name = 'MovBancarioForm.html'
    contexto = {'movForm': movForm}
    contexto.update(mov_bancarios_detalle_filtrar(request))
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.mov_bancario_agregar_dc", None, raise_exception=True)
def mov_bancario_agregar_dc(request):
    choices = DEBITO_CREDITO
    usuario_actual = Perfil.objects.get(user=request.user.pk)
    if request.POST:
        movForm = MovBancarioForm(request.POST, request.FILES, user=usuario_actual, choices=choices)
        if request.POST['submit'] == "Grabar movimiento":
            movForm.save()
            return redirect('mov_bancario_listar')
    else:
        movForm = MovBancarioForm(user=usuario_actual, choices=choices)

    template_name = 'MovBancarioForm.html'
    contexto = {'movForm': movForm}
    contexto.update(mov_bancarios_detalle_filtrar(request))
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.mov_bancario_editar", None, raise_exception=True)
def mov_bancario_editar(request, id):
    try:
        mov_bancario = MovBancario.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('mov_bancario_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        movForm = MovBancarioForm(post, request.FILES, instance=mov_bancario, id=id, choices=TIPO_MOV_BANCARIO)
        detallesForm = MovBancarios_DetalleForm(request.POST, request.FILES)
        if movForm.is_valid():
            movForm.save()
            return redirect('mov_bancario_listar')
    else:
        movForm = MovBancarioForm(instance=mov_bancario, id=id, choices=TIPO_MOV_BANCARIO)
        detallesForm = MovBancarios_DetalleForm()

    template_name = 'MovBancarioForm.html'
    contexto = {'movForm': movForm, 'detallesForm': detallesForm, 'MovBancario': MovBancario, 'id': id}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.mov_bancario_eliminar", None, raise_exception=True)
def mov_bancario_eliminar(request, id):
    url = 'mov_bancario_listar'
    try:
        mov_bancario = MovBancario.objects.get(id=id)
        mov_bancario.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


########################################################################################################################


@csrf_exempt
@login_required(login_url='ingresar')
@permission_required("bancos.mov_bancarios_detalle_eliminar", None, raise_exception=True)
def mov_bancarios_detalle_eliminar(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        try:
            detalle = MovBancarios_Detalle.objects.get(pk=id)
            detalle.delete()
            return JsonResponse({"status": 1})
        except Exception as e:
            pass
    return JsonResponse({"status": 0})


@login_required(login_url='ingresar')
def mov_bancarios_detalle_listar(request):
    if request.method == 'GET':
        mov_bancario_id = empty2none(request.GET['mov_bancario'])
        print(mov_bancario_id)
        detalles_list = list(MovBancarios_Detalle.objects.filter(mov_bancario=mov_bancario_id).values())
        for objeto in detalles_list:
            if objeto['medio_pago_id'] is not None:
                objeto['medio_pago_id'] = MedioDePago.objects.get(pk=objeto['medio_pago_id']).descripcion
            if objeto['vencimiento_det'] is not None:
                objeto['vencimiento_det'] = objeto['vencimiento_det'].strftime('%d/%m/%Y')

        success = 'guardado'
        return JsonResponse({"status": success, "detalles_data": detalles_list})
    else:
        success = 'todo mal'
        return JsonResponse({"status": success})


def empty2none(x):
    return x if x is not '' else None


@login_required(login_url='ingresar')
def mov_bancarios_detalle_agregar(request):
    if request.method == 'POST':
        print(f"{request.POST} + \n\n")

        mov_bancario_id = empty2none(request.POST.get('mov_bancario', None))
        if mov_bancario_id is not None and mov_bancario_id is not '':
            mov_bancario = MovBancario.objects.get(pk=mov_bancario_id)
        else:
            mov_bancario = None

        medio_pago_id = request.POST.get('medio_pago', None)
        if medio_pago_id is not None and medio_pago_id is not '':
            medio_pago = MedioDePago.objects.get(pk=medio_pago_id)
        else:
            medio_pago = None

        cheque = empty2none(request.POST.get('cheque', None))
        importe_det = empty2none(request.POST.get('importe_det', None))

        vencimiento_det_unparsed = request.POST.get('vencimiento_det', None)
        if vencimiento_det_unparsed is not None and vencimiento_det_unparsed is not '':
            vencimiento_det = datetime.strptime(vencimiento_det_unparsed, '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            vencimiento_det = None

        cheque_numero = empty2none(request.POST.get('cheque_numero', None))
        estado_anterior = empty2none(request.POST.get('estado_anterior', None))
        nuevo_detalle = MovBancarios_Detalle(mov_bancario=mov_bancario, medio_pago=medio_pago,
                                             cheque=cheque, importe_det=importe_det,
                                             vencimiento_det=vencimiento_det, cheque_numero=cheque_numero,
                                             estado_anterior=estado_anterior)
        nuevo_detalle.save()

        detalles_list = list(MovBancarios_Detalle.objects.filter(mov_bancario=mov_bancario_id).values())
        print(detalles_list)

        for objeto in detalles_list:
            if objeto['medio_pago_id'] is not None:
                objeto['medio_pago_id'] = MedioDePago.objects.get(pk=objeto['medio_pago_id']).descripcion
            if objeto['vencimiento_det'] is not None:
                objeto['vencimiento_det'] = objeto['vencimiento_det'].strftime('%d/%m/%Y')

        success = 'guardado'
        return JsonResponse({"status": success, "detalles_data": detalles_list})
    else:
        success = 'Todo mal'
        return JsonResponse({"status": success})


########################################################################################################################


@login_required(login_url='ingresar')
def cheques_terceros_listar(request):
    contexto = cheques_terceros_filtrar(request)
    template_name = 'cheques_terceros_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.cheques_terceros_agregar", None, raise_exception=True)
def cheques_terceros_agregar(request):
    if request.POST:
        form = Cheques_TercerosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cheques_terceros_listar')
    else:
        form = Cheques_TercerosForm()

    template_name = 'Cheques_TercerosForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.cheques_terceros_editar", None, raise_exception=True)
def cheques_terceros_editar(request, id):
    try:
        cheques_terceros = Cheques_Terceros.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('cheques_terceros_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = Cheques_TercerosForm(post, request.FILES, instance=cheques_terceros, id=id)
        if form.is_valid():
            form.save()
            return redirect('cheques_terceros_listar')
    else:
        form = Cheques_TercerosForm(instance=cheques_terceros, id=id)

    template_name = 'Cheques_TercerosForm.html'
    contexto = {'form': form, 'Cheques_Terceros': Cheques_Terceros}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("bancos.cheques_terceros_eliminar", None, raise_exception=True)
def cheques_terceros_eliminar(request, id):
    url = 'cheques_terceros_listar'
    try:
        cheques_terceros = Cheques_Terceros.objects.get(id=id)
        cheques_terceros.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)