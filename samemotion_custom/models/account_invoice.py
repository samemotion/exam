
from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = ['account.invoice']

    l10n_pe_document_serie = fields.Char("Document Serie")
    l10n_pe_document_number = fields.Char("Document Nr.")