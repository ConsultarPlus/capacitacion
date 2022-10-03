from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware

from finanzas.filters import caja_filtrar, caja_cierres_filtrar, cierres_medio_filtrar
from finanzas.forms import CajaForm, CajaCierresForm, CierresMedioForm
from finanzas.models import Caja, CierresMedio, CajaCierres


@login_required(login_url='ingresar')
def caja_listar(request):
    contexto = caja_filtrar(request)
    template_name = 'caja_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.caja_agregar", None, raise_exception=True)
def caja_agregar(request):
    if request.POST:
        form = CajaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('caja_listar')
    else:
        form = CajaForm()

    template_name = 'CajaForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.caja_editar", None, raise_exception=True)
def caja_editar(request, id):
    try:
        caja = Caja.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('caja_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = CajaForm(post, request.FILES, instance=caja)
        if form.is_valid():
            form.save()
            return redirect('caja_listar')
    else:
        form = CajaForm(instance=caja)

    template_name = 'CajaForm.html'
    contexto = {'form': form, 'Caja': Caja}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.caja_eliminar", None, raise_exception=True)
def caja_eliminar(request, id):
    url = 'caja_listar'
    try:
        caja = Caja.objects.get(id=id)
        caja.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


@login_required(login_url='ingresar')
def caja_cierres_listar(request):
    contexto = caja_cierres_filtrar(request)
    template_name = 'caja_cierres_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.caja_cierres_agregar", None, raise_exception=True)
def caja_cierres_agregar(request, id):
    if request.POST:
        form = CajaCierresForm(request.POST, request.FILES, caja=id)
        if form.is_valid():
            form.save()
            return redirect('caja_cierres_listar')
    else:
        form = CajaCierresForm(caja=id)

    template_name = 'CajaCierresForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.caja_cierres_eliminar", None, raise_exception=True)
def caja_cierres_eliminar(request, id):
    url = 'caja_cierres_listar'
    try:
        caja_cierres = CajaCierres.objects.get(numero=id)
        caja_cierres.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


@login_required(login_url='ingresar')
def cierres_medio_listar(request):
    contexto = cierres_medio_filtrar(request)
    template_name = 'cierres_medio_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.cierres_medio_agregar", None, raise_exception=True)
def cierres_medio_agregar(request, id):
    if request.POST:
        form = CierresMedioForm(request.POST, request.FILES, cierre=id)
        if form.is_valid():
            form.save()
            return redirect('caja_cierres_listar')
    else:
        form = CierresMedioForm(cierre=id)

    template_name = 'CierresMedioForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.cierres_medio_eliminar", None, raise_exception=True)
def cierres_medio_eliminar(request, id):
    url = 'caja_cierres_listar'
    try:
        cierres_medio = CierresMedio.objects.get(id=id)
        cierres_medio.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)
