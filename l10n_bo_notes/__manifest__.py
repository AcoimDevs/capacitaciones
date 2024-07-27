# -*- coding: utf-8 -*-
{
    'name': 'apuntes internos',
    'version': '1.0', 
    'author':'Acoim Ltda',
    'summary': 'Apuntes de usuarios',
    'depends':[
        'base',
        'base_setup',
        'purchase',
        'sale_management'
    ],
    'category': 'Notes',
    'data': [
        'security/ir.model.access.csv',
        'security//ir_rule.xml',
        'views/l10n_bo_notes.xml',
        'views/menuitem.xml',
        'reports/l10n_bo_notes_report.xml'
    ],
    'installable' : True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'webside': 'https://www.acoim.com/',
    'maintainer': '',
    'contributors':['luis', 'manuel','ale']

}