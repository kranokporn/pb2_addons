# -*- coding: utf-8 -*-
from openerp import fields, models


class AccountBudget(models.Model):
    _inherit = "account.budget"

    operating_unit_id = fields.Many2one(required=True)


class AccountBudgetLines(models.Model):
    _inherit = "account.budget.line"

    operating_unit_id = fields.Many2one(required=True)
