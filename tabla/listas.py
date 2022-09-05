
ENTIDADES = (
    ('ESTADO_CIVIL', 'Estados civiles'),
    ('RUBRO', 'Rubro'),
)

ACTIVO = (
    ('S', 'Activo'),
    ('N', 'Inactivo'),
)

SINO = (
    ('S', 'Sí'),
    ('N', 'No'),
)


PRIORIDAD = (
    ('A', 'Alta'),
    ('M', 'Media'),
    ('B', 'Baja'),
)

PRIORIDAD_MAS_VACIO = (('', '---'),) + PRIORIDAD

AMBITO = (
    ('N', 'Nacional'),
    ('P', 'Provincial'),
    ('M', 'Municipal'),
    ('A', 'Particular'),
)

AMBITO_TUP = dict(AMBITO)

APLICACIONES = (
    ('PERSONA', 'Persona'),
    ('EXPEDIENTE', 'Expediente'),
    ('COMPROBANTE', 'Comprobante'),
)


TIPOS_DE_VARIABLE = (
        ('F', 'Fecha'),
        ('C', 'Caracter'),
        ('N', 'Numérico'),
        ('L', 'Lógico'),
    )

ITEMS_X_PAG = (
    ('5', 'ver 5 ítems'),
    ('10', 'ver 10 ítems'),
    ('15', 'ver 15 ítems'),
    ('30', 'ver 30 ítems'),
    )

etiquetas_otros = (('{{ salto_de_pagina }}', 'Salto de página'),
                   ('{{ip <ID de plantilla>|incluir_plantilla ip}}', 'Incluir plantilla'))

grupos_de_etiquetas = (
    ('', 'Seleccionar tipo de etiquetas'),
)


HOJAS = (('A4', 'A4'),
         ('A5', 'A5'),
         ('CARTA', 'CARTA'),
         ('OFICIO', 'OFICIO'),
         ('LEGAL', 'LEGAL'),
         ('1/2 CARTA', '1/2 CARTA'),
         )


PREPOSICIONES = ('a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', '' +
                 'en', 'entre', 'hacia', 'hasta', 'para', 'por', 'según', 'segun', 'sin', '' +
                 'so', 'sobre', 'tras', 'durante', 'mediante', 'versus', 'vía', 'via', '' +
                 'y', 'o', 'u', 'ó', 'e', 'ni', 'no', 'si', 'sí')  # Estas últimas no son preposiciones, son nexos


MODELOS = (
           ('VARIABLE', 'Variables'),
           ('PLANTILLA', 'Plantillas'),
           ('TABLA', 'Tablas'),
           ('COMPROBANTES', 'Comprobantes'),
           ('NUMERADORES', 'Numeradores'),
           ('GENERAL', 'General'),
           ('DEPARTAMENTO', 'Departamento')
           )
