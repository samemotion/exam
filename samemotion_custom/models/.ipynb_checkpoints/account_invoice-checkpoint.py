
from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = ['account.invoice']

    l10n_pe_document_serie = fields.Char("Document Serie")
    l10n_pe_document_number = fields.Char("Document Nr.")

    team_id = fields.Many2one("crm.team", string="Canal de Ventas")

    issue_invoice_date = fields.Datetime("Fecha Emisión")

    def stock_move_ids_domain(self):
        return [('origin','=','%s' %(self.origin))]

    stock_move_ids = fields.One2many('stock.move','id', domain=stock_move_ids_domain)

    @api.onchange('sequence_number_next')
    def onchange_sequence_number_next(self):
        #Es preferible trabajar la secuencia (ir.sequence) sin / para no hacer replace
        self.l10n_pe_document_serie = str(self.sequence_number_next_prefix).replace("/","")
        self.l10n_pe_document_number = self.sequence_number_next

