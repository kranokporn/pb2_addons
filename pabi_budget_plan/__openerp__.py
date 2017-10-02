# -*- coding: utf-8 -*-
{
    'name': "NSTDA :: PABI2 Budget Preparation",
    'summary': "",
    'author': "Ecosoft",
    'website': "http://ecosoft.co.th",
    'category': 'Account',
    'version': '0.1.0',
    'depends': [
        'account_budget_activity',
        'pabi_chartfield',
        'pabi_procurement',
        'pabi_utils',
        # 'document_status_history',
    ],
    'data': [
        'security/security_rule_plan_unit.xml',
        'security/security_rule_breakdown.xml',
        'security/security_rule_budget_unit.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/actions.xml',
        'data/report_data.xml',
        'xlsx_template/templates.xml',
        # 'data/history_rule.xml',
        'views/budget_plan_menu.xml',
        # 'wizard/convert_to_budget_control_wizard.xml',
        'wizard/asset_plan_to_budget_plan_wizard.xml',
        'wizard/invest_asset_select_wizard_view.xml',
        'wizard/generate_budget_plan_wizard.xml',
        'wizard/budget_breakdown_action_excel_import_wizard.xml',
        'wizard/xlsx_template_wizard.xml',
        'views/account_budget_view.xml',
        'views/budget_plan_unit_view.xml',
        'views/budget_plan_project_view.xml',
        'views/budget_policy_view.xml',
        # 'views/budget_policy_report_view.xml',
        'views/budget_breakdown_view.xml',
        'views/budget_plan_personnel_view.xml',
        'views/budget_plan_invest_asset_view.xml',
        'views/budget_plan_invest_construction_view.xml',
        'views/invest_asset_plan_view.xml',
        'views/account_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
