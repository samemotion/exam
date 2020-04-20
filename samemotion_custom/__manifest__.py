# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# noinspection PyStatementEffect
{
    'name': 'samemotion_custom',
    'version': '1.0',
    'category': 'Sales/Point Of Sale',
    'sequence': 6,
    'summary': 'Customization for Point fof Sale',
    'description': """Customized features for Same Motion Evaluation""",
    'depends': ['crm','account'],
    'data': [
        # 'data/pos_sale_data.xml',
        # 'security/pos_sale_security.xml',
        # 'security/ir.model.access.csv',
        # 'views/sales_team_views.xml',
        # 'views/pos_config_views.xml',
        # 'views/pos_custom.xml',
        'views/account_invoice_view.xml',
        'report/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': True,
}
