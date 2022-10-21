from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect

from bancos.filters import cuenta_bancaria_filtrar, chequera_filtrar, mov_bancario_filtrar, \
    mov_bancarios_detalle_filtrar
from bancos.forms import ChequeraForm, CuentaBancariaForm, MovBancarioForm, MovBancarios_DetalleForm
from bancos.models import CuentaBancaria, Chequera, MovBancario, MovBancarios_Detalle
from perfiles.models import Perfil
from tabla.listas import TIPO_MOV_BANCARIO, DP_NE_CA_RE


@login_required(login_url='ingresar')
def cuenta_bancaria_listar(request):
    contexto = cuenta_bancaria_filtrar(request)
    template_name = 'cuenta_bancaria_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.cuenta_bancaria_agregar", None, raise_exception=True)
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
@permission_required("finanzas.cuenta_bancaria_editar", None, raise_exception=True)
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
@permission_required("finanzas.cuenta_bancaria_eliminar", None, raise_exception=True)
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


@login_required(login_url='ingresar')
def chequera_listar(request):
    contexto = chequera_filtrar(request)
    template_name = 'chequera_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.chequera_agregar", None, raise_exception=True)
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
@permission_required("finanzas.chequera_editar", None, raise_exception=True)
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
@permission_required("finanzas.chequera_eliminar", None, raise_exception=True)
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


@login_required(login_url='ingresar')
def mov_bancario_listar(request):
    contexto = mov_bancario_filtrar(request)
    template_name = 'mov_bancario_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.mov_bancario_agregar", None, raise_exception=True)
def mov_bancario_agregar(request):
    usuario_actual = Perfil.objects.get(user=request.user.pk)
    if request.POST:
        print(request.POST['submit'])
        movForm = MovBancarioForm(request.POST, request.FILES, user=usuario_actual, choices=DP_NE_CA_RE)
        detallesForm = MovBancarios_DetalleForm(request.POST, request.FILES)

        if request.POST['submit'] == "Grabar detalle" and detallesForm.is_valid():
            detallesForm.save()
            return redirect('mov_bancario_agregar')
        if request.POST['submit'] == "Grabar movimiento" and movForm.is_valid():
            movForm.save()
            return redirect('mov_bancario_listar')
    else:
        movForm = MovBancarioForm(user=usuario_actual, choices=DP_NE_CA_RE)
        detallesForm = MovBancarios_DetalleForm()

    template_name = 'MovBancarioForm.html'
    contexto = {'movForm': movForm,
                'detallesForm': detallesForm}
    contexto.update(mov_bancarios_detalle_filtrar(request))
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.mov_bancario_editar", None, raise_exception=True)
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
    contexto = {'movForm': movForm, 'detallesForm': detallesForm, 'MovBancario': MovBancario}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("finanzas.mov_bancario_eliminar", None, raise_exception=True)
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


@login_required(login_url='ingresar')
@permission_required("finanzas.mov_bancarios_detalle_eliminar", None, raise_exception=True)
def mov_bancarios_detalle_eliminar(request, id):
    url = 'mov_bancario_agregar'
    mov_bancarios_detalle = MovBancarios_Detalle.objects.get(pk=id)
    mov_bancarios_detalle.delete()
    return redirect(url)
