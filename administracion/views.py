from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from administracion.forms import DepartamentoForm, DepositoForm
from administracion.models import Departamento, Deposito
from .filters import departamento_filtrar, deposito_filtrar


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
def deposito_listar(request):
    contexto = deposito_filtrar(request)
    template_name = "deposito_listar.html"
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.deposito_agregar", None, raise_exception=True)
def deposito_agregar(request):
    if request.POST:
        form = DepositoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deposito_listar')
    else:
        form = DepositoForm()

    template_name = 'DepositoForm.html'
    contexto = {'form': form}
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
    contexto = {'form': form, 'Deposito': Deposito}
    return render(request, template_name, contexto)


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
