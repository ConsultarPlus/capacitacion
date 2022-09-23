from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from contabilidad.filters import plan_de_cuentas_filtrar, cuenta_contable_valida2
from contabilidad.forms import PlanDeCuentasForm
from contabilidad.models import PlanDeCuentas
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
