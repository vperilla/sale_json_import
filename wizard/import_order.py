import base64
import json
from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ImportOrder(models.TransientModel):
    _name = 'import.order'
    _description = 'Import Sale Order from JSON file'

    json_file = fields.Binary('JSON File')

    @api.multi
    def import_json_file(self):
        self.ensure_one()
        Order = self.env['sale.order']
        data = json.loads(base64.decodestring(self.json_file))['data']
        # To create an order first we need a customer
        Customer = self.env['res.partner']
        customer_data = data['customer']
        customer = Customer.search([
            ('email', '=', customer_data['email'])
        ])
        if customer:
            customer = customer[0]
        else:
            Country = self.env['res.country']
            State = self.env['res.country.state']
            customer_country = None
            customer_state = None
            country = Country.search([
                ('code', '=', customer_data['address']['country_code'])
            ])
            if country:
                customer_country = country[0]
                state = State.search([
                    ('name', '=', customer_data['address']['province'])
                ])
                if state:
                    customer_state = state[0]
                else:
                    customer_state = State.create({
                        'name': customer_data['address']['province'],
                        'country_id': customer_country.id,
                        'code': customer_data['address']['province'].lower(),
                    })
            customer_values = {
                'name': f"{customer_data['name']} {customer_data['surname']}",
                'phone': customer_data['phone'],
                'email': customer_data['email'],
                'country_id': customer_country.id,
                'state_id': customer_state.id if customer_state else None,
                'street': customer_data['address']['street'],
                'city': customer_data['address']['city'],
                'zip': customer_data['address']['postal_code']
            }
            customer = Customer.create(customer_values)
        order = Order.create({
            'partner_id': customer.id,
            'external': True,
            'external_id': data['id'],
            'external_date': datetime.strptime(
                data['date'][:-5], '%Y-%m-%dT%H:%M:%S'),
            'external_status': data['status'],
            'external_payment_method': data['payment_method'],
        })
        Product = self.env['product.product']
        Line = self.env['sale.order.line']
        for sequence, line in enumerate(data['lines']):
            product = Product.search([])[0]
            quantity = line['units']
            price = line['price_unit']
            description = line['name']
            quantity = line['units']
            order_line = Line.create({
                'order_id': order.id,
                'product_id': product.id,
                'name': description,
                'product_uom_qty': quantity,
                'price_unit': price,
                'sequence': sequence,
            })
        print('something')
