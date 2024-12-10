# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',# for initial, we can keep it as empty
    'category': 'Hospital',
    'author':'sasank',
    'sequence':-100,# for coming in first in applist in ui
    'summary': 'Hospital Managements Systems',
    'description': """ It's all about Hospital Managements Systems """,
    'depends': ['mail'], #inherited module will be stored into depends
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
    ],# all xml file will be loaded into the data.
    'demo': [],
    'application': True,# for making it domain application
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
    },
}
