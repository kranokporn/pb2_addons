# -*- coding: utf-8 -*-
{
    'name': 'Print Report from Journal Entries',
    'version': '8.0.0.1.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'author': "Ecosoft",
    'website': 'http://www.ecosoft.co.th/',
    'depends': [
        'pabi_account',
        'pabi_interface',
        'report_webkit',
        'l10n_th_amount_text',
    ],
    'data': [
        'data/paperformat.xml',
        'report/report.xml',
        'report/account_interface_report.xml',
        'report/invoice_refund_report.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
    'application': True,
}
