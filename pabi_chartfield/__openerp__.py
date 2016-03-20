# -*- coding: utf-8 -*-
{
    'name': "NSTDA :: PABI2 Account - Budget/Account Chart Field",
    'summary': "",
    'author': "Ecosoft",
    'website': "http://ecosoft.co.th",
    'category': 'Account',
    'version': '0.1.0',
    'depends': ['account_budget_activity',
                'pabi_base',
                'purchase_request_to_requisition',
                ],
    'data': [
        'views/account_budget_view.xml',
        'views/account_invoice_view.xml',
        'views/analytic_view.xml',
        'views/account_move_view.xml',
        'views/purchase_view.xml',
        'views/purchase_request_view.xml',
        'views/purchase_requisition_view.xml',
        #'report/account_analytic_entries_report_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
