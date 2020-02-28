# -*- coding: utf-8 -*-

import base64
from openerp import api, fields, models, _
from openerp.exceptions import Warning as UserError
import openerp.addons.decimal_precision as dp
from openerp.addons.l10n_th_amount_text.amount_to_text_th \
    import amount_to_text_th


class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_term = fields.Many2one('account.payment.term', string='Payment Terms')

    def _get_url_attachment(self, name):
        self.ensure_one()
        file_name = 'eTax' + name + '.pdf'
        move = self.env['account.move'].search([('name', '=', name)], limit=1)
        attachment_ids = self.env['ir.attachment'].search(
            [('res_model', '=', 'account.move'), ('res_id', '=', move.id)])
        if attachment_ids:
            return attachment_ids.filtered(lambda l: l.name == file_name).mapped('url')
        # file_prefix = self.env.user.company_id.pabiweb_file_prefix
        file_prefix = 'http://localhost:8069/report/pdf/'
        file_url = 'pabi_print_etax.invoice_refund_report/' + str(move.id)
        attachment = self.env['ir.attachment'].create({
            'res_id': move.id,
            'res_model': 'account.move',
            'name': file_name,
            'url': file_prefix + file_url,
            'type': 'url',
        })
        return attachment.url

    def _get_language(self):
        return self._context.get('lang', False)

    def _get_datas_invoice_refund(self):
        datas = {
            'amount_untaxed': 0.00,
            'tax': 0.00,
            'total': 0.00,
        }
        lines = {}
        for line in self.line_id:
            if line.date_maturity:
                datas['total'] += line.debit - line.credit
            else:
                if line.org_id:
                    if line.name not in lines.keys():
                        lines[line.name] = line._get_items()
                    else:
                        lines[line.name]['amount_untaxed'] += line.debit - line.credit
                    datas['amount_untaxed'] += line.debit - line.credit
                else:
                    datas['tax'] += line.debit - line.credit
        datas['lines'] = lines.values()
        datas['amount_untaxed'] = abs(datas['amount_untaxed'])
        datas['tax'] = abs(datas['tax'])
        datas['total'] = abs(datas['total'])
        datas['discount'] = abs(datas['total'] - datas['amount_untaxed'] - datas['tax'])
        datas['total_text_th'] = amount_to_text_th(datas['total'], self.company_id.currency_id.name)
        return datas

    # def _get_datas_account_interface(self):
    #     datas = {
    #         'amount_untaxed': 0.00,
    #         'tax': 0.00,
    #         'total': 0.00,
    #     }
    #     lines = {}
    #     tax = []
    #     for line in self.line_id:
    #         if line.date_maturity:
    #             datas['total'] += line.debit - line.credit
    #         else:
    #             if line.account_tax_id:
    #                 if self.document_id.type == 'invoive':
    #                     datas['tax'] += line.debit - line.credit
    #                 elif self.document_id.type == 'voucher':
    #                     if line.credit - line.debit in tax:
    #                         datas['tax'] += line.debit - line.credit
    #                     else:
    #                         tax.append(line.debit - line.credit)
    #             else:
    #                 if line.name not in lines.keys():
    #                     lines[line.name] = line._get_items()
    #                 else:
    #                     lines[line.name]['amount_untaxed'] += line.debit - line.credit
    #                 datas['amount_untaxed'] += line.debit - line.credit
    #     datas['lines'] = lines.values()
    #     datas['amount_untaxed'] = abs(datas['amount_untaxed'])
    #     datas['tax'] = abs(datas['tax'])
    #     datas['total'] = abs(datas['total'])
    #     datas['discount'] = abs(datas['total'] - datas['amount_untaxed'] - datas['tax'])
    #     datas['total_text_th'] = amount_to_text_th(datas['total'], self.company_id.currency_id.name)
    #     return datas


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    price_unit = fields.Float(string='Unit Price', required=True,
        digits= dp.get_precision('Product Price'), default=0.00)

    def _get_items(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'uom': self.product_uom_id.name,
            'price_unit': self.price_unit,
            'amount_untaxed': self.debit - self.credit,
        }
