from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from contabilidad.filters import plan_de_cuentas_filtrar, cuenta_contable_valida2, ejercicio_filtrar, asientos_filtrar, asientos_detalle_filtrar
from contabilidad.forms import PlanDeCuentasForm, EjercicioForm, AsientosForm, AsientosDetalleForm
from contabilidad.models import PlanDeCuentas, Ejercicio, Asientos, AsientosDetalle
from tabla.gets import get_variable


@login_required(login_url='ingresar')
def plan_de_cuentas_listar(request):
    contexto = plan_de_cuentas_filtrar(request)
    template_name = 'plan_de_cuentas_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.plan_de_cuentas_agregar", None, raise_exception=True)
def plan_de_cuentas_agregar(request):
    if request.POST:
        form = PlanDeCuentasForm(request.POST, request.FILES)
        if form.is_valid() and cuenta_contable_valida2(request, request.POST.dict()):
            form.save()
            return redirect('plan_de_cuentas_listar')
    else:
        form = PlanDeCuentasForm(V1=get_variable("V_N1", 1),
                                 V2=get_variable("V_N2", 1),
                                 V3=get_variable("V_N3", 2),
                                 V4=get_variable("V_N4", 2),
                                 V5=get_variable("V_N5", 2))

    template_name = 'PlanDeCuentasForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.plan_de_cuentas_editar", None, raise_exception=True)
def plan_de_cuentas_editar(request, id):
    try:
        plan_de_cuentas = PlanDeCuentas.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('plan_de_cuentas_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = PlanDeCuentasForm(post, request.FILES, instance=plan_de_cuentas)
        if form.is_valid() and cuenta_contable_valida2(request, request.POST.dict()):
            form.save()
            return redirect('plan_de_cuentas_listar')
    else:
        form = PlanDeCuentasForm(V1=get_variable("V_N1", 1),
                                 V2=get_variable("V_N2", 1),
                                 V3=get_variable("V_N3", 2),
                                 V4=get_variable("V_N4", 2),
                                 V5=get_variable("V_N5", 2),
                                 instance=plan_de_cuentas)

    template_name = 'PlanDeCuentasForm.html'
    contexto = {'form': form, 'PlanDeCuentas': PlanDeCuentas}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.plan_de_cuentas_eliminar", None, raise_exception=True)
def plan_de_cuentas_eliminar(request, id):
    url = 'plan_de_cuentas_listar'
    try:
        plan_de_cuentas = PlanDeCuentas.objects.get(id=id)
        plan_de_cuentas.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


@login_required(login_url='ingresar')
@permission_required('ejercicio.ejercicio_puede_listar', None, raise_exception=True)
def ejercicio_listar(request):
    contexto = ejercicio_filtrar(request)

    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'ejercicio_list_block.html'
    else:
        template_name = 'ejercicio_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("ejercicio.ejercicio_agregar", None, raise_exception=True)
def ejercicio_agregar(request):
    url = reverse('ejercicio_agregar')
    if request.POST:
        form = EjercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ejercicio_listar')
    else:
        form = EjercicioForm()

    template_name = 'EjercicioForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("ejercicio.ejercicio_editar", None, raise_exception=True)
def ejercicio_editar(request, id):
    try:
        ejercicio = Ejercicio.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('ejercicio_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = EjercicioForm(post, request.FILES, instance=ejercicio)
        if form.is_valid():
            form.save()
            return redirect('ejercicio_listar')
    else:
        form = EjercicioForm(instance=ejercicio)

    template_name = 'EjercicioForm.html'
    contexto = {'form': form, 'Ejercicio': Ejercicio}
    return render(request, template_name, contexto)



@login_required(login_url='ingresar')
@permission_required("ejercicio.ejercicio_eliminar", None, raise_exception=True)
def ejercicio_eliminar(request, id):
    url = 'ejercicio_listar'
    try:
        ejercicio = Ejercicio.objects.get(id=id)
        ejercicio.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required('asientos.asientos_puede_listar', None, raise_exception=True)
def asientos_listar(request):
    contexto = asientos_filtrar(request)
    print(contexto)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'asientos_list_block.html'
    else:
        template_name = 'asientos_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("asientos.asientos_agregar", None, raise_exception=True)
def asientos_agregar(request):
    url = reverse('asientos_agregar')
    if request.POST:
        form = AsientosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asientos_listar')
    else:
        form = AsientosForm()

    template_name = 'AsientosForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("asientos.asientos_editar", None, raise_exception=True)
def asientos_editar(request, id):
    try:
        asientos = Asientos.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('asientos_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = AsientosForm(post, request.FILES, instance=asientos)
        if form.is_valid():
            form.save()
            return redirect('ejercicio_listar')
    else:
        form = AsientosForm(instance=asientos)

    template_name = 'AsientosForm.html'
    contexto = {'form': form, 'Asientos': Asientos}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("asientos.asientos_eliminar", None, raise_exception=True)
def asientos_eliminar(request, id):
    url = 'asientos_listar'
    try:
        asientos = Asientos.objects.get(id=id)
        asientos.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required('asientosdetalle.asientos_detalle_puede_listar', None, raise_exception=True)
def asientos_detalle_listar(request):
    contexto = asientos_detalle_filtrar(request)

    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'asientosdetalle_list_block.html'
    else:
        template_name = 'asientos_detalle_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("asientosdetalle.asientos_detalle_agregar", None, raise_exception=True)
def asientos_detalle_agregar(request):
    url = reverse('asientos_detalle_agregar')
    if request.POST:
        form = AsientosDetalleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asientos_detalle_listar')
    else:
        form = AsientosDetalleForm()

    template_name = 'AsientosDetalleForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("asientosdetalle.asientos_detalle_editar", None, raise_exception=True)
def asientos_detalle_editar(request, id):
    try:
        asientosdetalle = AsientosDetalle.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('asientos_detalle_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = AsientosDetalleForm(post, request.FILES, instance=asientosdetalle)
        if form.is_valid():
            form.save()
            return redirect('asientos_detalle_listar')
    else:
        form = AsientosDetalleForm(instance=asientosdetalle)

    template_name = 'AsientosDetalleForm.html'
    contexto = {'form': form, 'AsientosDetalle': AsientosDetalle}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("asientosdetalle.asientos_detalle_eliminar", None, raise_exception=True)
def asientos_detalle_eliminar(request, id):
    url = 'asientos_detalle_listar'
    try:
        asientosdetalle = AsientosDetalle.objects.get(id=id)
        asientosdetalle.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)
