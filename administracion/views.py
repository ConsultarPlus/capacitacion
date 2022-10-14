from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from administracion.models import Viajante, Transporte, CondicionDePago, Deposito, MedioDePago, Moneda, Departamento,GrupoContactos, GrupoEconomico
from administracion.forms import ViajanteForm, TransporteForm, CondicionDePagoForm, DepartamentoForm, DepositoForm, MedioDePagoForm, MonedaForm, GrupoContactosForm, GrupoEconomicoForm
from administracion.filters import viajante_filtrar, transporte_filtrar, condiciondepago_filtrar, deposito_filtrar, mediodepago_filtrar, moneda_filtrar, departamento_filtrar, grupocontactos_filtrar, grupoeconomico_filtrar


@login_required(login_url='ingresar')
def departamento_listar(request):
    contexto = departamento_filtrar(request)
    template_name = 'departamento_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.departamento_agregar", None, raise_exception=True)
def departamento_agregar(request):
    if request.POST:
        form = DepartamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('departamento_listar')
    else:
        form = DepartamentoForm()

    template_name = 'DepartamentoForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.departamento_editar", None, raise_exception=True)
def departamento_editar(request, id):
    try:
        departamento = Departamento.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('departamento_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = DepartamentoForm(post, request.FILES, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('departamento_listar')
    else:
        form = DepartamentoForm(instance=departamento)

    template_name = 'DepartamentoForm.html'
    contexto = {'form': form, 'Departamento': Departamento}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.departamento_eliminar", None, raise_exception=True)
def departamento_eliminar(request, id):
    url = 'departamento_listar'
    try:
        departamento = Departamento.objects.get(id=id)
        departamento.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("administracion.viajante_puede_listar", None, raise_exception=True)
def viajante_listar(request):
    contexto = viajante_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'viajante_list_block.html'
    else:
        template_name = 'viajante_listar.html'

    return render(request, template_name, contexto)


@permission_required("administracion.viajante_editar", None, raise_exception=True)
def viajante_editar(request, id):
    try:
        viajante = Viajante.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('viajante_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = ViajanteForm(post, instance=viajante)
        if form.is_valid():
            form.save()
            return redirect('viajante_listar')
    else:
        form = ViajanteForm(instance=viajante)

    template_name = 'ViajanteForm.html'
    contexto = {'form': form, 'viajante': viajante}
    return render(request, template_name, contexto)



@permission_required("administracion.viajante_agregar", None, raise_exception=True)
def viajante_agregar(request):
    url = reverse('viajante_agregar')
    if request.POST:
        form = ViajanteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('viajante_listar')
    else:
        form = ViajanteForm(initial={'activos': 'S'})

    template_name = "ViajanteForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.viajante_eliminar", None, raise_exception=True)
def viajante_eliminar(request, id):
    url = 'viajante_listar'
    try:
        viajante = Viajante.objects.get(id=id)
        viajante.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("administracion.transporte_puede_listar", None, raise_exception=True)
def transporte_listar(request):
    contexto = transporte_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'transporte_list_block.html'
    else:
        template_name = 'transporte_listar.html'

    return render(request, template_name, contexto)


@permission_required("administracion.transporte_editar", None, raise_exception=True)
def transporte_editar(request, id):
    try:
        transporte = Transporte.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('transporte_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = TransporteForm(post, instance=transporte)
        if form.is_valid():
            form.save()
            return redirect('transporte_listar')
    else:
        form = TransporteForm(instance=transporte)

    template_name = 'TransporteForm.html'
    contexto = {'form': form, 'transporte': transporte}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.transporte_agregar", None, raise_exception=True)
def transporte_agregar(request):
    url = reverse('transporte_agregar')
    if request.POST:
        form = TransporteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('transporte_listar')
    else:
        form = TransporteForm(initial={'activos': 'S'})

    template_name = "TransporteForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.transporte_eliminar", None, raise_exception=True)
def transporte_eliminar(request, id):
    url = 'transporte_listar'
    try:
        transporte = Transporte.objects.get(id=id)
        transporte.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@permission_required("administracion.condiciondepago_puede_listar", None, raise_exception=True)
def condiciondepago_listar(request):
    contexto = condiciondepago_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'condiciondepago_list_block.html'
    else:
        template_name = 'condiciondepago_listar.html'

    return render(request, template_name, contexto)


@permission_required("administracion.condiciondepago_editar", None, raise_exception=True)
def condiciondepago_editar(request, id):
    try:
        condiciondepago = CondicionDePago.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('condiciondepago_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = CondicionDePagoForm(post, instance=condiciondepago)
        if form.is_valid():
            form.save()
            return redirect('condiciondepago_listar')
    else:
        form = CondicionDePagoForm(instance=condiciondepago)

    template_name = 'CondicionDePagoForm.html'
    contexto = {'form': form, 'condiciondepago': condiciondepago}
    return render(request, template_name, contexto)


@permission_required("administracion.condiciondepago_agregar", None, raise_exception=True)
def condiciondepago_agregar(request):
    url = reverse('condiciondepago_agregar')
    if request.POST:
        form = CondicionDePagoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('condiciondepago_listar')
    else:
        form = CondicionDePagoForm(initial={'activos': 'S'})

    template_name = "CondicionDePagoForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.condiciondepago_eliminar", None, raise_exception=True)
def condiciondepago_eliminar(request, id):
    url = 'condiciondepago_listar'
    try:
        condiciondepago = CondicionDePago.objects.get(id=id)
        condiciondepago.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("administracion.deposito_puede_listar", None, raise_exception=True)
def deposito_listar(request):
    contexto = deposito_filtrar(request)
    template_name = 'deposito_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.deposito_editar", None, raise_exception=True)
def deposito_editar(request, id):
    try:
        deposito = Deposito.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('deposito_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = DepositoForm(post, instance=deposito)
        if form.is_valid():
            form.save()
            return redirect('deposito_listar')
    else:
        form = DepositoForm(instance=deposito)

    template_name = 'DepositoForm.html'
    contexto = {'form': form, 'deposito': deposito}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.deposito_agregar", None, raise_exception=True)
def deposito_agregar(request):
    url = reverse('deposito_agregar')
    if request.POST:
        form = DepositoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('deposito_listar')
    else:
        form = DepositoForm(initial={'activos': 'S'})

    template_name = "DepositoForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.deposito_eliminar", None, raise_exception=True)
def deposito_eliminar(request, id):
    url = 'deposito_listar'
    try:
        deposito = Deposito.objects.get(id=id)
        deposito.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("administracion.mediodepago_puede_listar", None, raise_exception=True)
def mediodepago_listar(request):
    contexto = mediodepago_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'mediodepago_list_block.html'
    else:
        template_name = 'mediodepago_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.mediodepago_editar", None, raise_exception=True)
def mediodepago_editar(request, id):
    try:
        mediodepago = MedioDePago.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('mediodepago_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = MedioDePagoForm(post, instance=mediodepago)
        if form.is_valid():
            form.save()
            return redirect('mediodepago_listar')
    else:
        form = MedioDePagoForm(instance=mediodepago)

    template_name = 'MedioDePagoForm.html'
    contexto = {'form': form, 'mediodepago': mediodepago}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.mediodepago_agregar", None, raise_exception=True)
def mediodepago_agregar(request):
    url = reverse('mediodepago_agregar')
    if request.POST:
        form = MedioDePagoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('mediodepago_listar')
    else:
        form = MedioDePagoForm(initial={})

    template_name = "MedioDePagoForm.html"

    return render(request, template_name, {'form': form, 'moneda': Moneda})


@login_required(login_url='ingresar')
@permission_required("administracion.mediodepago_eliminar", None, raise_exception=True)
def mediodepago_eliminar(request, id):
    url = 'mediodepago_listar'
    try:
        mediodepago = MedioDePago.objects.get(id=id)
        mediodepago.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_puede_listar", None, raise_exception=True)
def moneda_listar(request):
    contexto = moneda_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'moneda_list_block.html'
    else:
        template_name = 'moneda_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_editar", None, raise_exception=True)
def moneda_editar(request, id):
    try:
        moneda = Moneda.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('moneda_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = MonedaForm(post, instance=moneda)
        if form.is_valid():
            form.save()
            return redirect('moneda_listar')
    else:
        form = MonedaForm(instance=moneda)

    template_name = 'MonedaForm.html'
    contexto = {'form': form, 'moneda': moneda}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_agregar", None, raise_exception=True)
def moneda_agregar(request):
    url = reverse('moneda_agregar')
    if request.POST:
        form = MonedaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('moneda_listar')
    else:
        form = MonedaForm(initial={'activos': 'S'})

    template_name = "MonedaForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_eliminar", None, raise_exception=True)
def moneda_eliminar(request, id):
    url = 'moneda_listar'
    try:
        moneda = Moneda.objects.get(id=id)
        moneda.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("administracion.grupocontactos_puede_listar", None, raise_exception=True)
def grupocontactos_listar(request):
    contexto = grupocontactos_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'grupocontactos_list_block.html'
    else:
        template_name = 'grupocontactos_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.grupocontactos_editar", None, raise_exception=True)
def grupocontactos_editar(request, id):
    try:
        grupocontactos = GrupoContactos.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('grupocontactos_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = GrupoContactosForm(post, instance=grupocontactos)
        if form.is_valid():
            form.save()
            return redirect('grupocontactos_listar')
    else:
        form = GrupoContactosForm(instance=grupocontactos)

    template_name = 'GrupoContactosForm.html'
    contexto = {'form': form, 'grupocontactos': grupocontactos}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.grupocontactos_agregar", None, raise_exception=True)
def grupocontactos_agregar(request):
    url = reverse('grupocontactos_agregar')
    if request.POST:
        form = GrupoContactosForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grupocontactos_listar')
    else:
        form = GrupoContactosForm(initial={'activos': 'S'})

    template_name = "GrupoContactosForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.grupocontactos_eliminar", None, raise_exception=True)
def grupocontactos_eliminar(request, id):
    url = 'grupocontactos_listar'
    try:
        grupocontactos = GrupoContactos.objects.get(id=id)
        grupocontactos.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)@login_required(login_url='ingresar')


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_puede_listar", None, raise_exception=True)
def moneda_listar(request):
    contexto = moneda_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'moneda_list_block.html'
    else:
        template_name = 'moneda_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_editar", None, raise_exception=True)
def moneda_editar(request, id):
    try:
        moneda = Moneda.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('moneda_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = MonedaForm(post, instance=moneda)
        if form.is_valid():
            form.save()
            return redirect('moneda_listar')
    else:
        form = MonedaForm(instance=moneda)

    template_name = 'MonedaForm.html'
    contexto = {'form': form, 'moneda': moneda}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_agregar", None, raise_exception=True)
def moneda_agregar(request):
    url = reverse('moneda_agregar')
    if request.POST:
        form = MonedaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('moneda_listar')
    else:
        form = MonedaForm(initial={'activos': 'S'})

    template_name = "MonedaForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.moneda_eliminar", None, raise_exception=True)
def moneda_eliminar(request, id):
    url = 'moneda_listar'
    try:
        moneda = Moneda.objects.get(id=id)
        moneda.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)@login_required(login_url='ingresar')



@login_required(login_url='ingresar')
@permission_required("administracion.grupoeconomico_puede_listar", None, raise_exception=True)
def grupoeconomico_listar(request):
    contexto = grupoeconomico_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'grupoeconomico_list_block.html'
    else:
        template_name = 'grupoeconomico_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.grupoeconomico_editar", None, raise_exception=True)
def grupoeconomico_editar(request, id):
    try:
        grupoeconomico = GrupoEconomico.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('grupoeconomico_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = GrupoEconomicoForm(post, instance=grupoeconomico)
        if form.is_valid():
            form.save()
            return redirect('grupoeconomico_listar')
    else:
        form = GrupoEconomicoForm(instance=grupoeconomico)

    template_name = 'GrupoEconomicoForm.html'
    contexto = {'form': form, 'grupoeconomico': grupoeconomico}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.grupoeconomico_agregar", None, raise_exception=True)
def grupoeconomico_agregar(request):
    url = reverse('grupoeconomico_agregar')
    if request.POST:
        form = GrupoEconomicoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('grupoeconomico_listar')
    else:
        form = GrupoEconomicoForm(initial={'activos': 'S'})

    template_name = "GrupoEconomicoForm.html"

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
@permission_required("administracion.grupoeconomico_eliminar", None, raise_exception=True)
def grupoeconomico_eliminar(request, id):
    url = 'grupoeconomico_listar'
    try:
        grupoeconomico = GrupoEconomico.objects.get(id=id)
        grupoeconomico.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)@login_required(login_url='ingresar')
