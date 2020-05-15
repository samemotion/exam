# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def _default_picking_transfer(self):
        type_obj = self.env['stock.picking.type']
        company_id = self.env.context.get('company_id') or self.env.user.company_id.id
        types = type_obj.search([('code', '=', 'outgoing'), ('warehouse_id.company_id', '=', company_id)], limit=1)
        if not types:
            types = type_obj.search([('code', '=', 'outgoing'), ('warehouse_id', '=', False)])
        return types[:4]

    date_submit = fields.Datetime(string=u'Fecha de emisión')
    team_type = fields.Selection([('sale', 'Venta directa'), ('website', 'Website')], string='Canal de ventas')
    picking_count = fields.Integer(string=u'N° de transferencias')
    invoice_picking_id = fields.Many2one('stock.picking', string='Transferencia de producto')
    picking_transfer_id = fields.Many2one('stock.picking.type', 'Tipo de transferencia', default=_default_picking_transfer)

    @api.multi
    def action_stock_picking(self):
        for order in self:
            if not order.invoice_line_ids:
                raise UserError(u'Crear facturación')
            if not self.number:
                raise UserError('Primero validar factura')
            if not self.invoice_picking_id:
                pick = {
                    'picking_type_id': self.picking_transfer_id.id,
                    'partner_id': self.partner_id.id,
                    'origin': self.number,
                    'location_dest_id': self.partner_id.property_stock_customer.id,
                    'location_id': self.picking_transfer_id.default_location_src_id.id
                }
                picking = self.env['stock.picking'].create(pick)
                self.invoice_picking_id = picking.id
                self.picking_count = len(picking)
                moves = order.invoice_line_ids.filtered(
                    lambda r: r.product_id.type in ['product', 'consu'])._create_stock_moves_transfer(picking)
                move_ids = moves._action_confirm()
                move_ids._action_assign()

    @api.multi
    def action_view_picking(self):
        action = self.env.ref('stock.action_picking_tree_ready')
        result = action.read()[0]
        result.pop('id', None)
        result['context'] = {}
        result['domain'] = [('id', '=', self.invoice_picking_id.id)]
        pick_ids = sum([self.invoice_picking_id.id])
        if pick_ids:
            res = self.env.ref('stock.view_picking_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = pick_ids or False
        return result 


class SupplierInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    def _create_stock_moves_transfer(self, picking):
            moves = self.env['stock.move']
            done = self.env['stock.move'].browse()
            for line in self:
                price_unit = line.price_unit
                template = {
                    'name': line.name or '',
                    'product_id': line.product_id.id,
                    'product_uom': line.uom_id.id,
                    'location_id': picking.picking_type_id.default_location_src_id.id,
                    'location_dest_id': line.invoice_id.partner_id.property_stock_customer.id,
                    'picking_id': picking.id,
                    'move_dest_id': False,
                    'state': 'draft',
                    'company_id': line.invoice_id.company_id.id,
                    'price_unit': price_unit,
                    'picking_type_id': picking.picking_type_id.id,
                    'procurement_id': False,
                    'route_ids': 1 and [
                        (6, 0, [x.id for x in self.env['stock.location.route'].search([('id', 'in', (2, 3))])])] or [],
                    'warehouse_id': picking.picking_type_id.warehouse_id.id,
                }
                diff_quantity = line.quantity
                tmp = template.copy()
                tmp.update({
                    'product_uom_qty': diff_quantity,
                })
                template['product_uom_qty'] = diff_quantity
                done += moves.create(template)
            return done