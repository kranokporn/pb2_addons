# -*- coding: utf-8 -*-
from openerp import models, api, fields, _
from openerp.exceptions import Warning


class AccountBudget(models.Model):
    _inherit = 'account.budget'

    BUDGETING_LEVEL = {'activity_group_id': 'Activity Group',
                       # 'activity_id': 'Activity',  # No activity level
                       # Project Based
                       'spa_id': 'SPA',
                       'mission_id': 'Mission',
                       'program_scheme_id': 'Program Scheme',
                       'program_group_id': 'Program Group',
                       'program_id': 'Program',
                       'project_group_id': 'Project Group',
                       'project_id': 'Project',
                       }

    BUDGETING_LEVEL_UNIT = {'activity_group_id': 'Activity Group',
                            # 'activity_id': 'Activity',  # No activity level
                            # Unit Based
                            'org_id': 'Org',
                            'sector_id': 'Sector',
                            'department_id': 'Department',
                            'division_id': 'Division',
                            'section_id': 'Section',
                            'costcenter_id': 'Costcenter',
                            }

    @api.model
    def _get_model_budgeting_level(self):
        MODEL_DICT = super(AccountBudget, self)._get_model_budgeting_level()
        MODEL_DICT.update({
            'spa_id': 'res.spa',
            'mission_id': 'res.mission',
            'tag_type_id': 'res.tag.type',
            'tag_id': 'res.tag',
            # Project Based
            'program_scheme_id': 'res.program.scheme',
            'program_group_id': 'res.program.group',
            'program_id': 'res.program',
            'project_group_id': 'res.project.group',
            'project_id': 'res.project',
            # Unit Based
            'org_id': 'res.org',
            'sector_id': 'res.sector',
            'department_id': 'res.department',
            'division_id': 'res.division',
            'section_id': 'res.section',
            'costcenter_id': 'res.costcenter',
        })
        return MODEL_DICT

    # -- Budget Check --
    @api.model
    def get_fiscal_and_budgeting_level(self, budget_date=False):
        """ Overwrite to get both project based and unit based """
        if not budget_date:
            budget_date = fields.Date.today()
        Fiscal = self.env['account.fiscalyear']
        fiscal_id = Fiscal.find(budget_date)
        fiscal = Fiscal.browse(fiscal_id)
        budgeting_level = fiscal.budgeting_level
        budgeting_level_unit = fiscal.budgeting_level_unit
        return fiscal_id, budgeting_level, budgeting_level_unit

    @api.model
    def _get_budgeting_resource(self, budgeting_resource_id, fiscal, *args):
        LEVEL = self.env['account.budget'].BUDGETING_LEVEL
        LEVEL_UNIT = self.env['account.budget'].BUDGETING_LEVEL_UNIT
        if args[0] == 'costcenter_id':
            model_dict = self._get_model_budgeting_level()
            model = model_dict.get(fiscal.budgeting_level_unit, False)
            if not budgeting_resource_id:
                field = LEVEL_UNIT[fiscal.budgeting_level_unit]
                raise Warning(_("Field %s is not entered, "
                                "can not check for budget") % (field,))
            resource = self.env[model].browse(budgeting_resource_id)
            return resource
        elif args[0] == 'project_id':
            if not budgeting_resource_id:
                field = LEVEL[fiscal.budgeting_level]
                raise Warning(_("Field %s is not entered, "
                                "can not check for budget") % (field,))
            return super(AccountBudget, self).\
                _get_budgeting_resource(budgeting_resource_id, fiscal)

    @api.model
    def _get_budget_monitor(self, resource, fiscal, *args):
        monitors = False
        if args[0] == 'costcenter_id':
            # 1st filter by fiscal
            monitors = resource.monitor_unit_ids.\
                filtered(lambda x: x.fiscalyear_id == fiscal)
            # 2nd filter by costcenter_id
            if fiscal.budgeting_level_unit in ('activity_group_id',
                                               'activity_id'):
                monitors = monitors.filtered(lambda x:
                                             x[args[0]].id == args[1])
        elif args[0] == 'project_id':
            # 1st filter by fiscal
            monitors = resource.monitor_ids.\
                filtered(lambda x: x.fiscalyear_id == fiscal)
            # 2nd filter by project_id
            if fiscal.budgeting_level in ('activity_group_id',
                                          'activity_id'):
                monitors = monitors.filtered(lambda x:
                                             x[args[0]].id == args[1])
        return monitors
