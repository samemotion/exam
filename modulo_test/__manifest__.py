# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Module Test',
    'version': '1.0',
    'category': '',
    'author': 'Miguel Canchachi Cano',
    'summary': 'Module Test',
    'description': """
        This module is a test.
    """,
    'depends': ['point_of_sale','account',],
    'data': [
        'views/account_move_view.xml',
        'report/account_invoice_report_template.xml',   
        
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
    'auto_install': False
}