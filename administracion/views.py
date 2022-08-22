from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from tabla.funcs import custom_redirect
from administracion.models import Viajante
from administracion.forms import ViajanteForm
from administracion.filters import viajante_filtrar


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


@login_required(login_url='ingresar')
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


@login_required(login_url='ingresar')
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
