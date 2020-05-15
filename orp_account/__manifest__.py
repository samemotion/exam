# -*- coding: utf-8 -*-

{
    'name': 'Commercial Account Invoice',
    'author': 'Omar Rodrigo Ruelas Príncipe',
    'category': 'Accounting',
    'description': """
Extensión del módulo de Facturación - Invoicing
--------------------------------------------------------------

Este módulo es apto para Odoo versión 12. Solicitado por SAME MOTION.
""",
    'summary': 'Commercial Invoice backported to Odoo 12.0 CE',
    'depends': ['account'],
    'data': [
        'views/account_invoice_views.xml',
        'report/report_account_invoice.xml',
    ]
}
