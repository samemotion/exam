# -*- coding: utf-8 -*-
from odoo import models, fields , api

class AccountInvoice(models.Model):
    _inherit =['account.invoice']


    serie = fields.Char(string='Nro de serie', store=True, compute="_compute_serie")

    correlative = fields.Char(string='Nro de correlativo',store=True)
    
    s_sale_channel = fields.Selection(string='Canal de ventas', selection=[('ev', 'Equipo de Ventas'), ('sw', 'Sitio Web'),])
    
    date_and_hour = fields.Datetime(string='Fecha de Emisión' , default=fields.Datetime.now)




    @api.depends('number')
    def _compute_serie(self):
        if(self.number != False):
            data1 = self.number[:8]
            serie = data1.replace('/','')
            self.serie = serie
            data2 = self.number[:-4]
            correlative = data2.replace('/','')
            self.correlative = correlative
    
 

     