from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from localidades.filters import pais_filtrar, provincia_filtrar, localidad_filtrar
from localidades.forms import PaisForm, ProvinciaForm, LocalidadForm
from localidades.models import Pais, Provincia, Localidad


@login_required(login_url='ingresar')
def pais_listar(request):
    contexto = pais_filtrar(request)
    template_name = 'pais_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.pais_agregar", None, raise_exception=True)
def pais_agregar(request):
    if request.POST:
        form = PaisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pais_listar')
    else:
        form = PaisForm()

    template_name = 'PaisForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.pais_editar", None, raise_exception=True)
def pais_editar(request, id):
    try:
        pais = Pais.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('pais_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = PaisForm(post, request.FILES, instance=pais)
        if form.is_valid():
            form.save()
            return redirect('pais_listar')
    else:
        form = PaisForm(instance=pais)

    template_name = 'PaisForm.html'
    contexto = {'form': form, 'Pais': Pais}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.pais_eliminar", None, raise_exception=True)
def pais_eliminar(request, id):
    url = 'pais_listar'
    try:
        pais = Pais.objects.get(id=id)
        pais.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


@login_required(login_url='ingresar')
def provincia_listar(request):
    contexto = provincia_filtrar(request)
    template_name = 'provincia_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.provincia_agregar", None, raise_exception=True)
def provincia_agregar(request):
    if request.POST:
        form = ProvinciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('provincia_listar')
    else:
        form = ProvinciaForm()

    template_name = 'ProvinciaForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.provincia_editar", None, raise_exception=True)
def provincia_editar(request, id):
    try:
        provincia = Provincia.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('provincia_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = ProvinciaForm(post, request.FILES, instance=provincia)
        if form.is_valid():
            form.save()
            return redirect('provincia_listar')
    else:
        form = ProvinciaForm(instance=provincia)

    template_name = 'ProvinciaForm.html'
    contexto = {'form': form, 'Provincia': Provincia}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.provincia_eliminar", None, raise_exception=True)
def provincia_eliminar(request, id):
    url = 'provincia_listar'
    try:
        provincia = Provincia.objects.get(id=id)
        provincia.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


@login_required(login_url='ingresar')
def localidad_listar(request):
    contexto = localidad_filtrar(request)
    template_name = 'localidad_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.localidad_agregar", None, raise_exception=True)
def localidad_agregar(request):
    if request.POST:
        form = LocalidadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('localidad_listar')
    else:
        form = LocalidadForm()

    template_name = 'LocalidadForm.html'
    contexto = {'form': form}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.localidad_editar", None, raise_exception=True)
def localidad_editar(request, id):
    try:
        localidad = Localidad.objects.get(id=id)
    except Exception as mensaje:
        messages.add_message(request, messages.ERROR, mensaje)
        return redirect('localidad_listar')

    if request.method == 'POST':
        post = request.POST.copy()
        form = LocalidadForm(post, request.FILES, instance=localidad)
        if form.is_valid():
            form.save()
            return redirect('localidad_listar')
    else:
        form = LocalidadForm(instance=localidad)

    template_name = 'LocalidadForm.html'
    contexto = {'form': form, 'Localidad': Localidad}
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("localidades.localidad_eliminar", None, raise_exception=True)
def localidad_eliminar(request, id):
    url = 'localidad_listar'
    try:
        localidad = Localidad.objects.get(id=id)
        localidad.delete()
    except Exception as e:
        mensaje = 'No se puede eliminar porque el ítem está referenciado en ' \
                  'otros registros. Otra opción es desactivarlo.'
        messages.add_message(request, messages.ERROR, mensaje)
    return redirect(url)


# funcion auxiliar para filtrar las provincias que se muestran en el filtro de busqueda según el país
def cargar_provincias(request):
    pais_id = request.GET.get('pais')

    if pais_id != '' and pais_id is not None:
        provincia = Provincia.objects.filter(pais=pais_id).order_by('descripcion')
    else:
        provincia = Provincia.objects.none()

    return render(request, 'provincias_dropdown.html', {'provincia': provincia})
