# -*- coding: utf-8 -*-
{
    'name': 'Hello Odoo',
    'version': '16.0.1.0.0',
    'summary': 'Training addon for managing greeting messages',
    'description': """
Hello Odoo
==========

A first training addon for an Odoo development lab. It introduces a simple
Greeting model with list, form, and search views.
    """,
    'category': 'Training',
    'author': 'Odoo Codex Lab',
    'website': 'https://example.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hello_odoo_greeting_views.xml',
        'views/hello_odoo_menus.xml',
    ],
    'demo': [
        'demo/hello_odoo_greeting_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
