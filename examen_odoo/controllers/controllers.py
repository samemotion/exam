# -*- coding: utf-8 -*-
from odoo import http

# class ExamenOdoo(http.Controller):
#     @http.route('/examen_odoo/examen_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_odoo/examen_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_odoo.listing', {
#             'root': '/examen_odoo/examen_odoo',
#             'objects': http.request.env['examen_odoo.examen_odoo'].search([]),
#         })

#     @http.route('/examen_odoo/examen_odoo/objects/<model("examen_odoo.examen_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_odoo.object', {
#             'object': obj
#         })