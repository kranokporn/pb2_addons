# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    url_attachment = fields.Char(
        string='URL',
        readonly=True,
    )

    @api.model
    def line_get_convert(self, line, part, date):
        res = super(AccountInvoice, self).line_get_convert(line, part, date)
        res.update({
            'price_unit': line.get('price_unit', 0.00),
        })
        return res

    @api.multi
    def button_print_attachment(self):
        self.ensure_one()
        url_attachment = self._get_url_attachment(self.move_id.name)
        self.url_attachment = url_attachment
