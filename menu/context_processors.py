from django.urls import reverse

from perfiles.funcs import get_preferencia
from tabla.templatetags.custom_tags import traducir


def menu_processor(request):
    css_version = '?v=1.2'
    usuario = request.user
    if usuario.is_authenticated:
        fijar_menu = get_preferencia(usuario, 'menu', 'fijar', 'L', False)
        modo_obscuro = get_preferencia(usuario, 'menu', 'modo_obscuro', 'L', False)

        # ADMINISTRACIÓN
        viajante_puede_listar = request.user.has_perm('administracion.viajante_puede_listar')
        transporte_puede_listar = request.user.has_perm('administracion.transporte_puede_listar')
        condiciondepago_puede_listar = request.user.has_perm('administracion.condiciondepago_puede_listar')
        deposito_puede_listar = request.user.has_perm('administracion.deposito_puede_listar')
        mediodepago_puede_listar = request.user.has_perm('administracion.mediodepago_puede_listar')
        moneda_puede_listar = request.user.has_perm('administracion.moneda_puede_listar')

        # CONFIGURACIÓN
        mostrar_admin = False
        if request.user.is_staff or request.user.is_superuser:
            mostrar_admin = True
        numerador_puede_listar = request.user.has_perm('numeradores.numerador_puede_listar')
        tabla_puede_listar = request.user.has_perm('tablas.tabla_puede_listar')
        variable_puede_listar = request.user.has_perm('tablas.variable_puede_listar')
        departamento_puede_listar = request.user.has_perm('administracion.administracion_puede_listar')
        pais_puede_listar = request.user.has_perm('localidades.pais_puede_listar')
        provincia_puede_listar = request.user.has_perm('localidades.provincia_puede_listar')
        localidad_puede_listar = request.user.has_perm('localidades.localidad_puede_listar')
        documento_puede_listar = request.user.has_perm('documentos.puede_listar')
        plantilla_puede_listar = request.user.has_perm('tabla.plantilla_puede_listar')
        plan_de_cuentas_puede_listar = request.user.has_perm('contabilidad.plan_de_cuentas_puede_listar')
        caja_puede_listar = request.user.has_perm('finanzas.caja_puede_listar')
        cuenta_bancaria_puede_listar = request.user.has_perm('bancos.cuenta_bancaria_puede_listar')
        chequera_puede_listar = request.user.has_perm('bancos.chequera_puede_listar')

        grupo_administracion_mostrar = False
        grupo_config_mostrar = False

        if viajante_puede_listar:
            grupo_administracion_mostrar = True

        if numerador_puede_listar or tabla_puede_listar or variable_puede_listar or mostrar_admin or documento_puede_listar or plantilla_puede_listar:
            grupo_config_mostrar = True

        grupos = [
                  {'id': 'ADM', 'descripcion': 'Administración',
                   'mostrar': get_preferencia(usuario, 'menu', 'ADM', 'L', False), 'visible': grupo_administracion_mostrar},
                  {'id': 'LOC', 'descripcion': 'Localidades',
                   'mostrar': get_preferencia(usuario, 'menu', 'LOC', 'L', False), 'visible': grupo_administracion_mostrar},
                  {'id': 'CBL', 'descripcion': 'Contabilidad',
                   'mostrar': get_preferencia(usuario, 'menu', 'CBL', 'L', False), 'visible': grupo_administracion_mostrar},
                  {'id': 'FNZ', 'descripcion': 'Finanzas',
                   'mostrar': get_preferencia(usuario, 'menu', 'FNZ', 'L', False), 'visible': grupo_administracion_mostrar},
                  {'id': 'BNC', 'descripcion': 'Bancos',
                   'mostrar': get_preferencia(usuario, 'menu', 'BNC', 'L', False), 'visible': grupo_administracion_mostrar},
                  {'id': 'CFN', 'descripcion': 'Configuración',
                   'mostrar': get_preferencia(usuario, 'menu', 'CFN', 'L', False), 'visible': grupo_config_mostrar},
                  ]

        menues = [
                  {'id_grupo': 'ADM', 'url': reverse('viajante_listar'), 'titulo': 'Viajantes', 'modelo': 'VIAJANTE',
                   'visible': viajante_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('transporte_listar'), 'titulo': 'Transportes',
                   'modelo': 'TRANSPORTE', 'visible': transporte_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('condiciondepago_listar'), 'titulo': 'Condiciónes De Pagos',
                   'modelo': 'CONDICIONDEPAGO', 'visible': condiciondepago_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('deposito_listar'), 'titulo': 'Depósitos',
                   'modelo': 'DEPOSITO', 'visible': deposito_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('mediodepago_listar'), 'titulo': 'Medios De Pago',
                   'modelo': 'MEDIODEPAGO', 'visible': mediodepago_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('moneda_listar'), 'titulo': 'Monedas',
                   'modelo': 'MONEDA', 'visible': moneda_puede_listar},
                  {'id_grupo': 'CFN', 'url': '/admin/', 'titulo': 'Admin', 'modelo': 'GENERAL',
                   'visible': mostrar_admin},
                  {'id_grupo': 'CFN', 'url': reverse('documentos_listar'), 'titulo': 'Documentos',
                   'modelo': 'DOCUMENTO', 'visible': documento_puede_listar},
                  {'id_grupo': 'CFN', 'url': reverse('plantillas_listar'), 'titulo': 'Plantillas',
                   'modelo': 'PLANTILLA', 'visible': plantilla_puede_listar},
                  {'id_grupo': 'CFN', 'url': reverse('numeradores_listar'), 'titulo': 'Numeradores',
                   'modelo': 'NUMERADOR',
                   'visible': numerador_puede_listar},
                  {'id_grupo': 'CFN', 'url': reverse('tablas_listar'), 'titulo': 'Tablas', 'modelo': 'TABLA',
                   'visible': tabla_puede_listar},
                  {'id_grupo': 'CFN', 'url': reverse('variables_listar'), 'titulo': 'Variables', 'modelo': 'VARIABLE',
                   'visible': variable_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('departamento_listar'), 'titulo': 'Departamentos',
                   'modelo': 'DEPARTAMENTO', 'visible': departamento_puede_listar},
                  {'id_grupo': 'ADM', 'url': reverse('deposito_listar'), 'titulo': 'Depósitos',
                   'modelo': 'DEPOSITO', 'visible': deposito_puede_listar},
                  {'id_grupo': 'LOC', 'url': reverse('pais_listar'), 'titulo': 'Países',
                   'modelo': 'PAIS', 'visible': pais_puede_listar},
                  {'id_grupo': 'LOC', 'url': reverse('provincia_listar'), 'titulo': 'Provincias',
                   'modelo': 'PROVINCIAS', 'visible': provincia_puede_listar},
                  {'id_grupo': 'LOC', 'url': reverse('localidad_listar'), 'titulo': 'Localidades',
                   'modelo': 'LOCALIDAD', 'visible': localidad_puede_listar},
                  {'id_grupo': 'CBL', 'url': reverse('plan_de_cuentas_listar'), 'titulo': 'Planes de cuentas',
                   'modelo': 'PLAN_DE_CUENTAS', 'visible': plan_de_cuentas_puede_listar},
                  {'id_grupo': 'FNZ', 'url': reverse('caja_listar'), 'titulo': 'Cajas',
                   'modelo': 'CAJA', 'visible': caja_puede_listar},
                  {'id_grupo': 'BNC', 'url': reverse('cuenta_bancaria_listar'), 'titulo': 'Cuentas bancarias',
                   'modelo': 'CUENTA_BANCARIA', 'visible': cuenta_bancaria_puede_listar},
                  {'id_grupo': 'BNC', 'url': reverse('chequera_listar'), 'titulo': 'Chequeras',
                   'modelo': 'CHEQUERA', 'visible': chequera_puede_listar},
                  ]

        for menu in menues:
            menu['titulo'] = traducir(menu['titulo'], menu['modelo'])

        carpeta_media = request.build_absolute_uri('/media/')
        return {'menues': menues,
                'grupos': grupos,
                'fijar_menu': fijar_menu,
                'css_version': css_version,
                'modo_obscuro': modo_obscuro,
                'carpeta_media': carpeta_media}
    else:
        return {}
