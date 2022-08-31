from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from capacitacion.settings import MEDIA_ROOT
from administracion.forms import DepartamentoForm
from administracion.models import Departamento
from .filters import administracion_filtrar


"""@login_required(login_url='ingresar')
@permission_required("administracion.administracion_puede_listar", None, raise_exception=True)
def administracion_listar(request):
    contexto = administracion_filtrar(request)
    codigo = request.GET.get('codigo')
    contexto['codigo'] = codigo
    contexto['url_filtros'] = request.GET.urlencode()
    return render(request, 'departamento_listar.html', contexto)"""


@login_required(login_url='ingresar')
def departamento_listar(request):
    contexto = administracion_filtrar(request)
    # print(MEDIA_ROOT)
    # print(contexto['filter'].first().imagen)
    # modo = request.GET.get('modo')
    # contexto['modo'] = modo
    # if modo == 'm' or modo == 's':
    #    at template_name = 'departamento_list_block.html'
    # else:
    #     template_name = 'departamento_listar.html'
    template_name = 'departamento_listar.html'
    return render(request, template_name, contexto)


@login_required(login_url='ingresar')
@permission_required("administracion.departamento_agregar", None, raise_exception=True)
def departamento_agregar(request):
    if request.POST:
        form = DepartamentoForm(request.POST, request.FILES)
        if form.is_valid():
            print("se guardó")
            print(form)
            print(form.save())
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
                  'otros registros. Otra opción es desactivarlo'
        messages.add_message(request, messages.ERROR, mensaje)

    return redirect(url)