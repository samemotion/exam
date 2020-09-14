# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from . import qr_code_base

class accountMove(models.Model):
    _inherit = 'account.move'

    qr_image = fields.Binary(string="Código QR", compute="_generate_qr_code")
    numero_serie = fields.Char(string="Número de serie", compute="_generate_num_serie")
    numero_correlativo = fields.Char(string="Número correlativo", compute="_generate_num_correlativo")
    canal_ventas = fields.Many2one('crm.team', string="Canal de ventas")
    fecha_emision = fields.Datetime("Fecha de emisión")
    mov_inventario = fields.Many2one('stock.move',string="Movimientos de Inventario")

    def _generate_num_serie(self):
        serie_correlativo = self.name.split('-')
        self.numero_serie = serie_correlativo[0]

    def _generate_num_correlativo(self):
        serie_correlativo = self.name.split('-')
        self.numero_correlativo = serie_correlativo[-1]

    def _generate_qr_code(self):
        qr_string = self._obtener_campos_qr()
        self.qr_image = qr_code_base.generate_qr_code(qr_string)

    def _obtener_campos_qr(self):
        qr_string = self.name + "|" + self.partner_id.name + "|" + str(self.invoice_date) + "|" + str(self.amount_total)
        return qr_string