# -*- coding: utf-8 -*-
import psycopg2
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import ValidationError


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    amount_retention = fields.Float(
        string='Retention',
        digits=dp.get_precision('Account'),
        readonly=True,
        states={'draft': [('readonly', False)]},
    )
    retention_on_payment = fields.Boolean(
        string='Retention on Payment',
        compute='_compute_retention_on_payment',
        store=True,
        help="If checked, retention will done during payment",
    )
    move_ids = fields.One2many(
        'account.move.line',
        related='move_id.line_id',
        string='Journal Items',
        readonly=True,
    )
    date_paid = fields.Date(
        string='Paid Date',
        compute='_compute_date_paid',
        store=True,
    )

    @api.multi
    @api.depends('state')
    def _compute_date_paid(self):
        for rec in self:
            if rec.state == 'paid' and rec.payment_ids:
                rec.date_paid = max(rec.payment_ids.mapped('date'))
            elif rec.state == 'open':
                rec.date_paid = False

    @api.multi
    @api.depends('invoice_line.price_subtotal',
                 'tax_line.amount',
                 'amount_retention')
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        for rec in self:
            rec.amount_tax = sum(line.amount for line in rec.tax_line)
            amount_total = rec.amount_untaxed + rec.amount_tax
            if not rec.retention_on_payment:
                rec.amount_total = amount_total - rec.amount_retention  # RET
            else:
                rec.amount_total = amount_total

    @api.multi
    @api.depends('partner_id')
    def _compute_retention_on_payment(self):
        for rec in self:
            rec.retention_on_payment = \
                self.env.user.company_id.retention_on_payment

    @api.multi
    def invoice_pay_customer(self):
        res = super(AccountInvoice, self).invoice_pay_customer()
        if res:
            res['context']['default_amount'] = 0.0
        return res

    @api.multi
    def action_move_create(self):
        try:
            with self._cr.savepoint():
                return super(AccountInvoice, self).action_move_create()
        except psycopg2.OperationalError:
            # Let's retry 3 times, each to wait 1 seconds
            retry = self._context.get('retry', 1)
            if retry <= 5:
                self._cr.rollback()
                retry += 1
                return self.with_context(retry=retry).action_move_create()
            raise ValidationError(
                _('Waiting for next number, please try again!'))
        except Exception:
            raise


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.model
    def move_line_get(self, invoice_id):

        res = super(AccountInvoiceLine, self).move_line_get(invoice_id)
        inv = self.env['account.invoice'].browse(invoice_id)

        if inv.amount_retention > 0.0 and not inv.retention_on_payment:
            sign = -1
            # sign = inv.type in ('out_invoice','in_invoice') and -1 or 1
            account_id = False
            company = self.env.user.company_id
            if inv.type in ('out_invoice', 'out_refund'):
                account_id = company.account_retention_customer.id
            else:
                account_id = company.account_retention_supplier.id
            if not account_id:
                raise ValidationError(
                    _('No account for retention has been configured!'))
            res.append({
                'type': 'src',
                'name': _('Retention Amount'),
                'price_unit': sign * inv.amount_retention,
                'quantity': 1,
                'price': sign * inv.amount_retention,
                'account_id': account_id,
                'product_id': False,
                'uos_id': False,
                'account_analytic_id': False,
                'taxes': False,
            })
        return res


class AccountInvoiceTax(models.Model):
    _inherit = 'account.invoice.tax'

    tax_code_type = fields.Selection(
        [('normal', 'Normal'),
         ('undue', 'Undue'),
         ('wht', 'Withholding')],
        string='Tax Code Type',
        related='tax_code_id.tax_code_type',
        store=True,
        help="Type based on Tax using this Tax Code",
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
