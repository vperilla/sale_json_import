# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    external = fields.Boolean('Is external')
    external_date = fields.Date('Date', readonly=True)
    external_id = fields.Integer('ID', readonly=True)
    external_status = fields.Char('Status', readonly=True)
    external_payment_method = fields.Selection([
        ('credit-card', 'Credit Card'),
    ], 'Payment Method', readonly=True)
