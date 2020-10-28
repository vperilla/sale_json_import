from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ImportOrder(models.TransientModel):
    _name = 'import.order'
    _description = 'Import Sale Order from JSON file'

    json_file = fields.Binary('JSON File')

    @api.multi
    def import_json_file(self):
        self.ensure_one()
        pass
