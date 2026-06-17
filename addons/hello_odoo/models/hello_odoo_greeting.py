# -*- coding: utf-8 -*-

from odoo import fields, models


class HelloOdooGreeting(models.Model):
    """Greeting message used by the Hello Odoo training addon."""

    _name = 'hello.odoo.greeting'
    _description = 'Greeting'
    _order = 'title'

    title = fields.Char(required=True)
    message = fields.Text()
    active = fields.Boolean(default=True)
