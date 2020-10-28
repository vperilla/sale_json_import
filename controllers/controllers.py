# -*- coding: utf-8 -*-
from odoo import http

# class SaleJsonImport(http.Controller):
#     @http.route('/sale_json_import/sale_json_import/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_json_import/sale_json_import/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_json_import.listing', {
#             'root': '/sale_json_import/sale_json_import',
#             'objects': http.request.env['sale_json_import.sale_json_import'].search([]),
#         })

#     @http.route('/sale_json_import/sale_json_import/objects/<model("sale_json_import.sale_json_import"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_json_import.object', {
#             'object': obj
#         })