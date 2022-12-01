from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from urllib.parse import urlencode
from clientes.models import Cliente, Tipos_Iva, CliEma
from clientes.forms import ClienteForm, Tipos_IvaForm, CliEmaForm
from clientes.filters import clientes_filtrar, tipos_iva_filtrar, cliema_filtrar
from tabla.forms import ImportarCSVForm
from tabla.funcs import es_valido, email_valido
from perfiles.admin import agregar_a_errores
from perfiles.models import Perfil
import random
import string


# Create your views here.
@login_required(login_url='ingresar')
@permission_required('clientes.puede_listar', None, raise_exception=True)
def clientes_listar(request):
    contexto = clientes_filtrar(request)
    modo = request.GET.get('modo')
    contexto['modo'] = modo

    if modo == 'm' or modo == 's':
        template_name = 'clientes_list_block.html'
    else:
        template_name = 'clientes_listar.html'

    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.cliente_agregar", None, raise_exception=True)
def cliente_agregar(request):
    url = reverse('cliente_agregar')
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            encriptado = ''.join(random.choice(string.ascii_lowercase.join(string.digits)) for i in range(10))
            nuevo_cliente = form.save()
            cliente = Cliente.objects.get(clicod=form.cleaned_data['clicod'])
            cliente.encriptado = encriptado
            cliente.save()
            return redirect('cliente_editar', id=nuevo_cliente.pk)
    else:
        form = ClienteForm()

    template_name = 'cliente_form.html'

    return render(request, template_name, {'form': form})


@login_required(login_url='ingresar')
# @permission_required("clientes.cliente_editar", None, raise_exception=True)
def cliente_editar(request, id, encriptado=None):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('menu')

    if request.method == 'POST':
        post = request.POST.copy()
        form = ClienteForm(post, instance=cliente, id=id)
        post["encriptado"] = encriptado
        if form.is_valid():
            form.save()
            return redirect('clientes_listar')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('menu')
    else:
        form = ClienteForm(instance=cliente, id=id)

    template_name = 'cliente_form.html'
    contexto = {'form': form, 'cliente': cliente}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.cliente_eliminar", None, raise_exception=True)
def cliente_eliminar(request, id):
    url = reverse('clientes_listar')
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("clientes.cliente_agregar", None, raise_exception=True)
def cliente_agregar_y_volver(request):
    url = reverse('cliente_agregar')
    parametros = urlencode({'volver': True})
    url = '{}?{}'.format(url, parametros)

    return redirect(url)


@login_required(login_url='ingresar')
@permission_required("clientes.cliente_importar", None, raise_exception=True)
def clientes_cargar_csv(request):
    errores_lista = []
    initial = {'entidades': (('CLIENTES', 'Clientes'),),
               'entidad': 'CLIENTES'}
    if request.POST:
        form = ImportarCSVForm(request.POST, request.FILES, initial=initial)
        if form.is_valid():
            csv = request.FILES['archivo']
            entidad = form.cleaned_data['entidad']
            actualizados = 0
            nuevos = 0
            errores = 0
            exitos = 0
            msj = ''
            try:
                for cnt, line in enumerate(csv):
                    try:
                        line_aux = line.decode("utf-8-sig")
                        if line_aux:
                            values = line_aux.split(';')
                            clicod = values[0].replace("'", "")
                            clicod = clicod.replace('"', '')
                            if len(clicod) > 10:
                                clicod = clicod[0:10]
                            clicod = clicod.upper()
                            nombre = ''
                            cuit = ''
                            domicilio = ''
                            telefono = ''
                            email = ''
                            saldo_inicial = ''
                            fecha_saldo = ''
                            encriptado = ''
                            if len(values) > 1:
                                nombre = values[1].replace("'", "").strip()
                                if len(nombre) > 100:
                                    nombre = nombre[0:97] + '...'
                                if len(values) > 2:
                                    cuit = values[2].strip()
                                    if len(values) > 3:
                                        domicilio = values[3].strip()
                                        if len(values) > 4:
                                            telefono = values[4].strip()
                                            if len(values) > 5:
                                                email = values[5].strip()
                                                if len(values) > 6:
                                                    saldo_inicial = values[6].strip()
                                                    if len(values) > 7:
                                                        fecha_saldo = values[7].strip()
                            activo = 'S'
                            valor_preferencial = 'N'
                            try:
                                cliente = Cliente.objects.get(clicod=clicod)
                                cliente.clicod = clicod
                                cliente.encriptado = ''.join(
                                    random.choice(string.ascii_lowercase.join(string.digits)) for i in range(10))
                                if nombre:
                                    cliente.nombre = nombre.upper()
                                if domicilio:
                                    cliente.domicilio = domicilio.upper()
                                if telefono:
                                    cliente.telefono = telefono
                                if email:
                                    cliente.email = email
                                if saldo_inicial:
                                    cliente.saldo_inicial = saldo_inicial
                                if fecha_saldo:
                                    cliente.fecha_saldo = fecha_saldo
                                if encriptado:
                                    encriptado = ''.join(
                                        random.choice(string.ascii_lowercase.join(string.digits)) for i in range(10))
                                cliente.save()
                                actualizados += 1
                                exitos += 1
                            except Cliente.DoesNotExist:
                                encriptado = ''.join(
                                    random.choice(string.ascii_lowercase.join(string.digits)) for i in range(10))
                                cliente = Cliente(clicod=clicod,
                                                  nombre=nombre.upper(),
                                                  cuit=cuit,
                                                  domicilio=domicilio.upper(),
                                                  telefono=telefono,
                                                  email=email,
                                                  saldo_inicial=saldo_inicial,
                                                  fecha_saldo=fecha_saldo,
                                                  encriptado=encriptado)
                                cliente.save()
                                nuevos += 1
                                exitos += 1

                            ok = True
                            if es_valido(email):
                                if email_valido(email):
                                    if User.objects.filter(email=email).exclude(username=clicod).exists():
                                        errores += 1
                                        e = 'El e-mail principal de ' + clicod + ' "' + email + \
                                            '" ya está asignado a otro usuario. ' + \
                                            'Se deja vacío'
                                        errores_lista = agregar_a_errores(cnt, errores, e, errores_lista)
                                        ok = False
                                else:
                                    errores += 1
                                    e = 'El e-mail principal de ' + clicod + ' "' + email + \
                                        '" no es válido. Se deja vacío'
                                    errores_lista = agregar_a_errores(cnt, errores, e, errores_lista)
                                    ok = False

                            if ok:
                                try:
                                    user = User.objects.get(username=clicod)
                                    user.first_name = nombre
                                    user.email = email
                                    user.save()
                                    actualizados += 1
                                    exitos += 1
                                except User.DoesNotExist:
                                    user = User.objects.create_user(username=clicod,
                                                                    first_name=nombre,
                                                                    email=email,
                                                                    is_active=True,
                                                                    )
                                    user.set_password('xadminweb')
                                    user.save()
                                    nuevos += 1
                                    exitos += 1
                                try:
                                    grupo = Group.objects.get(name='Clientes')
                                    grupo.user_set.add(user)
                                    perfil, creado = Perfil.objects.get_or_create(user_id=user.id)
                                    perfil.clicod = clicod
                                    perfil.save()
                                except Exception as e:
                                    e = 'Problemas con el grupo o el perfil.'
                                    errores_lista = agregar_a_errores(cnt, errores, e, errores_lista)

                    except Exception as e:
                        errores += 1
                        if errores <= 10:
                            if errores == 10:
                                errores_lista.append('Hay más errores...')
                            else:
                                errores_lista.append('Fila {}: {}'.format(cnt + 1, e))
            except Exception as e:
                msj = e

            if msj:
                messages.add_message(request, messages.ERROR, msj)
            else:
                msj = 'Carga de {}: {} errores; {} actualizados; {} nuevos'.format(entidad, errores,
                                                                                   actualizados, nuevos)
                if errores_lista:
                    messages.add_message(request, messages.ERROR, msj)
                else:
                    messages.add_message(request, messages.INFO, msj)
                    return redirect('tablas_listar')
    else:
        form = ImportarCSVForm(initial=initial)

    template_name = 'tabla/tabla_form.html'
    formato = 'CliCod C(5) ; Nombre C(100); CUIT C(13); Domicilio C(60); Teléfono C(60); E-mail C(60); Saldo N(12.2) ' \
              'Codificación UTF-8'
    titulo = 'Importar CSV'
    contexto = {'form': form, 'formato': formato, 'errores': errores_lista, 'titulo': titulo}
    return render(request, template_name, contexto)


########################################################################################################################


@login_required(login_url='ingresar')
def tipos_iva_listar(request):
    contexto = tipos_iva_filtrar(request)
    template_name = 'tipos_iva_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.tipos_iva_agregar", None, raise_exception=True)
def tipos_iva_agregar(request):
    if request.POST:
        form = Tipos_IvaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tipos_iva_listar')
    else:
        form = Tipos_IvaForm()

    template_name = 'Tipos_IvaForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.tipos_iva_editar", None, raise_exception=True)
def tipos_iva_editar(request, id):
    try:
        tipos_iva = Tipos_Iva.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('tipos_iva_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = Tipos_IvaForm(post, request.FILES, instance=tipos_iva)
        if form.is_valid():
            form.save()
            return redirect('tipos_iva_listar')
    else:
        form = Tipos_IvaForm(instance=tipos_iva)

    template_name = 'Tipos_IvaForm.html'
    contexto = {'form': form, 'Tipos_Iva': Tipos_Iva}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.tipos_iva_eliminar", None, raise_exception=True)
def tipos_iva_eliminar(request, id):
    url = 'tipos_iva_listar'
    try:
        tipos_iva = Tipos_Iva.objects.get(id=id)
        tipos_iva.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


########################################################################################################################


@login_required(login_url='ingresar')
def cliema_listar(request, id):
    contexto = cliema_filtrar(request, id)
    template_name = 'cliema_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.cliema_agregar", None, raise_exception=True)
def cliema_agregar(request, id):
    if request.POST:
        form = CliEmaForm(request.POST, request.FILES, initial={'cliente': Cliente.objects.get(pk=id)})
        if form.is_valid():
            form.save()
            return redirect('cliema_listar', id=id)
    else:
        form = CliEmaForm(initial={'cliente': Cliente.objects.get(pk=id)})

    template_name = 'CliEmaForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.cliema_editar", None, raise_exception=True)
def cliema_editar(request, cliente_id, id):
    try:
        cliema = CliEma.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('cliema_listar', id=cliente_id)

    if request.method == 'POST':
        post = request.POST.copy()
        form = CliEmaForm(post, request.FILES, instance=cliema)
        if form.is_valid():
            form.save()
            return redirect('cliema_listar', id=cliente_id)
    else:
        form = CliEmaForm(instance=cliema)

    template_name = 'CliEmaForm.html'
    contexto = {'form': form, 'CliEma': CliEma}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("clientes.cliema_eliminar", None, raise_exception=True)
def cliema_eliminar(request, cliente_id, id):
    url = 'cliema_listar'
    try:
        cliema = CliEma.objects.get(id=id)
        cliema.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url, id=cliente_id)